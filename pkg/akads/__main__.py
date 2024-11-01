"""
Command-line interface for documentation generation.

For command-line usage:
    # Development mode
    python -m pkg.akads --mode dev --json-path .tmp/tree_project.json

    # Production mode (default)
    python -m pkg.akads --json-path .tmp/tree_project.json
"""

import argparse
from .run import run

def main():
    """
    Parse command line arguments and run the documentation generator.
    """
    parser = argparse.ArgumentParser(description="Generate documentation from project structure")
    parser.add_argument("--mode", choices=["prod", "dev"], default="prod",
                      help="Running mode: prod (production) or dev (development)")
    parser.add_argument("--json-path", default=".tmp/tree_project.json",
                      help="Path to JSON file containing project structure")
    args = parser.parse_args()
    
    run(args.json_path, args.mode)

if __name__ == "__main__":
    main()
