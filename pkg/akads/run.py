"""
Core implementation of the documentation generator.
"""

import importlib.util
import sys
import os
from typing import Dict, Any
from utils.get_base_path import get_base_path
from utils.load_json import load_json
from . import run_doc_react
from . import run_doc_sass

def process_structure(json_data: Dict[str, Any], mode: str) -> None:
    """
    Process the JSON structure and run appropriate documentation generators.

    Args:
        json_data (Dict[str, Any]): The loaded JSON structure to process.
        mode (str): Running mode, either "prod" or "dev"
    """
    # Check for React structure
    if "react" in json_data and "src" in json_data["react"]:
        try:
            run_doc_react.run(json_data, mode)
        except Exception as e:
            print(f"Error processing React documentation: {e}")
    
    # Check for Sass structure
    if "sass" in json_data and "src" in json_data["sass"]:
        try:
            run_doc_sass.run(json_data, mode)
        except Exception as e:
            print(f"Error processing Sass documentation: {e}")

def run(json_path: str = ".tmp/tree_project.json", mode: str = "prod") -> None:
    """
    Runs the documentation generation process.
    
    Args:
        json_path (str): Path to the JSON structure file
        mode (str): Running mode, either "prod" or "dev" (default: "prod")
            - "prod": Running from .nexus in another repository
            - "dev": Running locally from codex repository
    """
    try:
        # Get base path for the current mode
        base = get_base_path(mode)
        
        # Load and validate JSON structure
        json_data = load_json(json_path)
        
        # Process the structure
        process_structure(json_data, mode)
        
    except Exception as e:
        print(f"Error processing documentation: {e}")
        sys.exit(1)
