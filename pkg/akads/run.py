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
    found_structures = False

    # Check for React structure
    if "react" in json_data and "src" in json_data["react"]:
        found_structures = True
        print("📝 Processing React documentation...")
        try:
            run_doc_react.run(json_data, mode)
            print("✅ React documentation processed successfully")
        except Exception as e:
            print(f"❌ Error processing React documentation: {e}")
    
    # Check for Sass structure
    if "sass" in json_data and "src" in json_data["sass"]:
        found_structures = True
        print("📝 Processing Sass documentation...")
        try:
            run_doc_sass.run(json_data, mode)
            print("✅ Sass documentation processed successfully")
        except Exception as e:
            print(f"❌ Error processing Sass documentation: {e}")

    if not found_structures:
        print("\n⚠️  No React or Sass structures found in the JSON data")
        print("💡 Make sure your JSON file contains 'react' and/or 'sass' sections with 'src' data")

def run(json_path: str = ".tmp/tree_project.json", mode: str = "prod") -> None:
    """
    Runs the documentation generation process.
    
    Args:
        json_path (str): Path to the JSON structure file
        mode (str): Running mode, either "prod" or "dev" (default: "prod")
            - "prod": Running from .codex in another repository
            - "dev": Running locally from codex repository
    """
    print(f"\n🚀 Starting documentation generation in {mode} mode...\n")
    print(f"📂 Using JSON file: {json_path}")

    try:
        # Get base path for the current environment
        base = get_base_path()
        print(f"📍 Base path: {base}")
        
        # Load and validate JSON structure
        print("📖 Loading JSON structure...")
        json_data = load_json(json_path)
        print("✅ JSON structure loaded successfully")
        
        # Process the structure
        process_structure(json_data, mode)
        
    except FileNotFoundError:
        print(f"❌ Error: JSON file not found: {json_path}")
        print("💡 Run tree_generate_all.sh first to generate the JSON structure")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error processing documentation: {e}")
        sys.exit(1)

    print("\n✨ Documentation generation complete!\n")
