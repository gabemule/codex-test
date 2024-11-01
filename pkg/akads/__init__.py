"""
Documentation generation module.

For programmatic usage:
    # Development mode
    from pkg.akads import run
    run(json_path=".tmp/project_structure.json", command_path="path/to/command.py", mode="dev")

    # Production mode (default)
    from .nexus.pkg.akads import run
    run(json_path=".tmp/project_structure.json", command_path="path/to/command.py")
"""

from .run import run

__all__ = ['run']
