"""
Documentation generation module.

For programmatic usage:
    # Development mode
    from pkg.akads import run
    run(json_path=".tmp/tree_project.json", mode="dev")

    # Production mode (default)
    from .nexus.pkg.akads import run
    run(json_path=".tmp/tree_project.json")  # mode defaults to "prod"
"""

from .run import run

__all__ = ['run']
