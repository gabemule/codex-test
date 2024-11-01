"""
React documentation processing implementation.

This module contains the implementation for processing React project structure
and generating documentation based on different command strategies.
"""

import os
import subprocess
from typing import Dict, Any, List
from utils.get_base_path import get_base_path

# File patterns to exclude
EXCLUDED_EXTENSIONS = [
    '.test.ts',
    '.test.tsx',
    '.d.ts',
    '.mock.ts',
    '.mock.tsx'
]

EXCLUDED_PREFIXES = [
    'index'
]

# Required extensions for story files
STORY_REQUIRED_EXTENSIONS = [
    '.tsx',
    '.stories.tsx',
    '.config.ts'
]

# Required extensions for component files
COMPONENT_REQUIRED_EXTENSIONS = [
    '.tsx',
    '.config.ts'
]

def display_command(files: List[str], dir_path: str, mode: str = "prod") -> None:
    """
    Generates and displays the command for the given set of files.

    Args:
        files (List[str]): List of files to be documented.
        dir_path (str): Current directory path.
        mode (str): Running mode, either "prod" or "dev" (default: "prod")
    """
    # Get base path for the current mode
    base = get_base_path(mode)

    # Join all file names into a single string, separated by space
    add_files = " ".join(files)

    # Add dir_path prefix to each file name
    react_files = " ".join(f"{dir_path}/{file}" for file in files)

    # Calculate documentation path
    # 1. Remove 'react/src' from the beginning of dir_path (first occurrence only)
    # 2. Remove any slash at the start or end of resulting path
    relative_path = dir_path.replace('react/src', '', 1).strip('/')
    
    # Build final documentation path:
    # - If relative_path is not empty, use 'docs/react/{relative_path}'
    # - If relative_path is empty (we're at react/src root), use just 'docs/react'
    doc_path = f"docs/react/{relative_path}" if relative_path else "docs/react"
    
    guidelines = f'--read {base}/prompts/react.md'
    message = f'--message "{doc_path}"'
    command = f"aider --subtree-only --no-auto-commit --yes --sonnet --cache-prompts --no-stream {guidelines} {message} {react_files}"

    print(f"\nfiles: {files}")
    print(f"\nrun_command: \n {command} \n")

    # Helper function to get the base name of a file (without extension)
    def get_base_name(file):
        return file.split('.')[0]

    # Process story files
    story_files = {}
    for file in files:
        if file.endswith('.stories.tsx'):
            base_name = get_base_name(file).replace('.stories', '')
            if all(f"{base_name}{ext}" in files for ext in STORY_REQUIRED_EXTENSIONS):
                story_files[base_name] = [f"{base_name}{ext}" for ext in STORY_REQUIRED_EXTENSIONS]

    # Process component files
    component_files = {}
    for file in files:
        if (file.endswith('.tsx') and 
            not file.endswith('.stories.tsx') and 
            not any(file.endswith(ext) for ext in EXCLUDED_EXTENSIONS)):
            base_name = get_base_name(file)
            if f"{base_name}.config.ts" in files:
                component_files[base_name] = [f"{base_name}{ext}" for ext in COMPONENT_REQUIRED_EXTENSIONS]

    # Process remaining ts files
    ts_files = []
    for file in files:
        base_name = get_base_name(file)
        if ((file.endswith('.ts') or file.endswith('.tsx')) and
            not any(file.startswith(prefix) for prefix in EXCLUDED_PREFIXES) and
            not any(file.endswith(ext) for ext in EXCLUDED_EXTENSIONS) and
            base_name not in story_files and
            base_name not in component_files and
            file not in [item for sublist in story_files.values() for item in sublist] and
            file not in [item for sublist in component_files.values() for item in sublist]):
            ts_files.append(file)

    # Print results
    if story_files:
        print("\nRun Storybook Doc:")
        print(story_files)
    if component_files:
        print("\nRun Component Doc:")
        print(component_files)
    if ts_files:
        print("\nRun TS Doc:")
        print(ts_files)

    # Check if there is any files to process
    if story_files or component_files or ts_files:
        print()
        print("-" * 80)

def process_directory(json: Dict[str, Any], current_path: str = "", mode: str = "prod") -> None:
    """
    Recursively processes a directory and displays commands for found files.

    Args:
        json (Dict[str, Any]): Directory structure to process.
        current_path (str): Current path in directory structure.
        mode (str): Running mode, either "prod" or "dev" (default: "prod")
    """
    for key, value in json.items():
        if key == '__snapshots__':
            continue
        if key == 'files':
            if value:
                display_command(value, current_path, mode)
        else:
            new_path = os.path.join(current_path, key)
            process_directory(value, new_path, mode)

def run(json: Dict[str, Any], mode: str = "prod") -> None:
    """
    Processes the React src directory structure and displays commands for found files.

    Args:
        json (Dict[str, Any]): The complete JSON structure.
        mode (str): Running mode, either "prod" or "dev" (default: "prod")
    """
    print("-" * 80)
    print("Starting - React Docs:")
    print("-" * 80)
    process_directory(json["react"]["src"], "react/src", mode)
    print("Processing completed.")
    print("-" * 80)
