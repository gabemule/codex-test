# Changelog Generator

This module runs aider to generate formatted changelogs. The changelog command can be used in two modes:
- **dev**: Running directly from the codex-test repository
- **prod**: Running from .nexus/project when codex-test is cloned as .nexus in another repository

## Usage Patterns

### Command-line Usage (via __main__.py)

Development mode:
```bash
python -m project.changelog --mode dev
```

Production mode (default):
```bash
python -m project.changelog
```

### Programmatic Usage (via __init__.py)

Development mode:
```python
from project.changelog import run
run(mode="dev")
```

Production mode (default):
```python
from .nexus.project.changelog import run
run()
```

## Complete Workflows

### Development Mode

When working directly in the codex-test repository:

```bash
# 1. Activate virtual environment (only needed once)
source scripts/start.sh

# 2. Install requirements (only needed once)
python -m project.changelog.requirements

# 3. Generate file trees (needed before each changelog generation)
python -m utils.file_tree.gen_all_trees

# 4. Generate changelog (choose one):
python -m project.changelog --mode dev  # Command-line usage
# or
python3 -c "from project.changelog import run; run(mode='dev')"  # Programmatic usage
```

### Production Mode

When using codex-test as a tool in another repository:

```bash
# 1. Clone codex-test as .nexus
git clone https://github.com/your-org/codex-test.git .nexus

# 2. Activate virtual environment (only needed once)
source .nexus/scripts/start.sh

# 3. Install requirements (only needed once)
python -m .nexus/project.changelog.requirements

# 4. Generate file trees (needed before each changelog generation)
python -m .nexus/utils.file_tree.gen_all_trees

# 5. Generate changelog (choose one):
python -m .nexus/project.changelog  # Command-line usage
# or
python3 -c "from .nexus.project.changelog import run; run()"  # Programmatic usage

# 6. Optional: Clean up when done
rm -rf .nexus
```

## Command Details

The generator runs the following aider command (paths shown for production mode):

```bash
aider \
  --subtree-only \
  --no-git \
  --yes \
  --sonnet \
  --cache-prompts \
  --no-stream \
  --read .nexus/project/changelog/template.md \
  --message-file .nexus/project/changelog/prompt.md \
  .tmp/commit_full_log.txt
```

## Directory Structure

### Development Mode (in codex-test repository)
```
project/
└── changelog/
    ├── __init__.py          # Handles programmatic usage exports
    ├── __main__.py         # Handles command-line interface
    ├── cli.py              # Core implementation
    ├── requirements.py      # Handles package installation
    ├── template.md         # Template for changelog generation
    └── prompt.md          # Instructions for changelog generation

utils/
└── file_tree/
    └── gen_all_trees.py   # Generates file trees used by changelog
```

### Production Mode (in another repository)
```
your-project/
└── .nexus/               # Cloned codex-test repository
    └── project/
        ├── changelog/    # Same structure as development mode
        └── utils/        # Same structure as development mode
```

## Usage Notes

1. Virtual environment activation and requirements installation only need to be done once
2. File trees must be generated before each changelog generation
3. Choose between command-line usage (via __main__.py) or programmatic usage (via __init__.py)
4. Default mode is "prod" when no mode is specified
5. Core implementation is in cli.py, independent of usage pattern
