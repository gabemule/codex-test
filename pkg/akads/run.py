"""
Core implementation of the documentation generator.
"""

import importlib.util
import sys
import os
from utils.get_base_path import get_base_path
from utils.load_json import load_json

def load_command(command_path: str):
    """
    Dynamically loads the command module.

    Args:
        command_path (str): Path to the command file.

    Returns:
        module: The loaded command module.
    """
    spec = importlib.util.spec_from_file_location("command", command_path)
    command = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(command)
    return command

def run(json_path: str = ".tmp/tree_akads.json", 
        command_path: str = "pkg/akads/run_docs.py",
        mode: str = "prod") -> None:
    """
    Runs the documentation generation process.
    
    Args:
        json_path (str): Path to the JSON structure file
        command_path (str): Path to the command file
        mode (str): Running mode, either "prod" or "dev" (default: "prod")
            - "prod": Running from .nexus in another repository
            - "dev": Running locally from codex-test repository
    """
    try:
        # Get base path for the current mode
        base = get_base_path(mode)
        
        # Adjust paths based on mode
        command_path = os.path.join(base, command_path)
        
        # Load and validate JSON structure
        json_data = load_json(json_path)
        
        # Load and validate command
        command = load_command(command_path)
        
        if not hasattr(command, 'run') or not callable(command.run):
            raise AttributeError("Command module must have a callable 'run' function")
        
        # Execute command with JSON structure
        command.run(json_data)
        
    except Exception as e:
        print(f"Error processing documentation: {e}")
        sys.exit(1)
