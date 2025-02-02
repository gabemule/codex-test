"""
Sass documentation processing implementation.

This module contains the implementation for processing Sass project structure
and generating documentation based on different command strategies.
"""

import os
import subprocess
from typing import Dict, Any, List
from utils.get_base_path import get_base_path

# File patterns to exclude
EXCLUDED_EXTENSIONS = [
    '.test.scss',
    '.min.scss'
]

EXCLUDED_PREFIXES = [
    '_'
]

def format_scss_info(file: str, dir_path: str) -> Dict[str, str]:
    """
    Format SCSS file information into a structured dictionary.

    Args:
        file (str): SCSS file name
        dir_path (str): Directory path for the file

    Returns:
        Dict[str, str]: Structured SCSS file information
    """
    base_name = file.split('.')[0]
    return {
        "name": base_name,
        "file": file,
        "path": dir_path
    }

def display_command(files: List[str], dir_path: str, mode: str = "prod") -> None:
    """
    Generates and displays the command for the given set of files.

    Args:
        files (List[str]): List of files to be documented.
        dir_path (str): Current directory path.
        mode (str): Running mode, either "prod" or "dev" (default: "prod")
    """
    # Get base path for the current environment
    base = get_base_path()

    # Join all file names into a single string, separated by space
    add_files = " ".join(files)

    # Add dir_path prefix to each file name
    sass_files = " ".join(f"{dir_path}/{file}" for file in files)

    # Calculate documentation path
    relative_path = dir_path.replace('sass/src', '', 1).strip('/')
    doc_path = f"docs/sass/{relative_path}" if relative_path else "docs/sass"
    
    base_aider = f"aider --subtree-only --no-auto-commit --yes --sonnet --cache-prompts --no-stream --no-check-update" 
    guidelines = f'--read "{doc_path}"'
    message = f'--message-file "{base}/pkg/akads/prompts/sass.md"'
    command = f"{base_aider} {guidelines} {message} {sass_files}"

    # print(f"\nFiles: {files}")
    # print(f"sass_files: {sass_files}")
    # print(f"relative_path: sass/src/{relative_path}")
    # print(f"doc_path: {doc_path}/README.md") 
    # print(f"\nrun_command: \n {command}")

    # Process scss files
    scss_files = []
    for file in files:
        if (file.endswith('.scss') and
            not any(file.startswith(prefix) for prefix in EXCLUDED_PREFIXES) and
            not any(file.endswith(ext) for ext in EXCLUDED_EXTENSIONS)):
            scss_files.append(format_scss_info(file, dir_path))

    # Print results
    if scss_files:
        print("\nRun SCSS Doc:")
        for info in scss_files:
            print(info)
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
        if key == 'files':
            if value:
                display_command(value, current_path, mode)
        else:
            new_path = os.path.join(current_path, key)
            process_directory(value, new_path, mode)

def run(json: Dict[str, Any], mode: str = "prod") -> None:
    """
    Processes the Sass src directory structure and displays commands for found files.

    Args:
        json (Dict[str, Any]): The complete JSON structure.
        mode (str): Running mode, either "prod" or "dev" (default: "prod")
    """
    print("-" * 80)
    print("Starting - Sass Docs:")
    print("-" * 80)
    process_directory(json["sass"]["src"], "sass/src", mode)
    print("Processing completed.")
    print("-" * 80)
