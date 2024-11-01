# Documentation Generator

This module runs documentation generation based on a JSON structure file and a command module. The documentation generator can be used in two modes:
- **dev**: Running directly from the codex-test repository
- **prod**: Running from .nexus/pkg when codex-test is cloned as .nexus in another repository

## Usage Patterns

### Command-line Usage (via __main__.py)

Development mode (in codex-test repository):
```bash
python -m pkg.akads --mode dev --json-path .tmp/project_structure.json
```

Production mode (in repository with .nexus):
```bash
python -m pkg.akads --json-path .tmp/project_structure.json
```

### Programmatic Usage (via __init__.py)

Development mode (in codex-test repository):
```python
from pkg.akads import run
run(json_path=".tmp/project_structure.json", mode="dev")
```

Production mode (in repository with .nexus):
```python
from .nexus.pkg.akads import run
run(json_path=".tmp/project_structure.json")
```

## Built-in Documentation Commands

The module includes built-in commands for documentation generation in `run_docs.py`:

### React Component Documentation
Generates documentation for React components including:
- Component name and path
- Description
- Props
- Usage examples

### Style File Documentation
Generates documentation for style files including:
- Style file name and path
- Description
- Usage examples

### Utility Documentation
Generates documentation for utility files including:
- Utility name and path
- Description
- Usage examples

## Parameters

- **json_path**: Path to the JSON file containing the project structure
  - Default: `.tmp/project_structure.json`
  - The JSON file should contain the project structure to be processed

- **command_path**: Path to the Python command file to execute
  - Default: `pkg/akads/run_docs.py`
  - The path is automatically adjusted based on mode using utils/get_base_path.py
  - In prod mode: `.nexus/pkg/akads/run_docs.py`
  - In dev mode: `./pkg/akads/run_docs.py`

- **mode**: Running mode, either "prod" or "dev"
  - Default: "prod"
  - "prod": Running from .nexus in another repository
  - "dev": Running directly from codex-test repository

## Path Handling

The module uses `utils/get_base_path.py` to handle paths correctly in both production and development modes:

```python
from utils.get_base_path import get_base_path

base = get_base_path(mode)  # Returns ".nexus" for prod, "." for dev
```

This ensures that files are accessed from the correct location whether running in development mode (directly from codex-test) or production mode (from .nexus in another repository).

## Command Module Requirements

The command module (specified by command_path) must:
1. Have a `run(json_data)` function
2. Accept the JSON structure as its parameter
3. Process the structure according to its specific documentation needs

Example command module:
```python
def run(json_data):
    """
    Process the JSON structure and generate documentation.
    
    Args:
        json_data: The loaded JSON structure to process
    """
    # Process json_data and generate documentation
    pass
```

## Directory Structure

### Development Mode (in codex-test repository)
```
pkg/
└── akads/
    ├── __init__.py          # Handles programmatic usage exports
    ├── __main__.py         # Handles command-line interface
    ├── run.py              # Core implementation
    ├── run_docs.py        # Built-in documentation commands
    └── README.md          # This documentation

utils/
├── get_base_path.py       # Path handling for dev/prod modes
└── load_json.py          # JSON loading utility
```

### Production Mode (in another repository)
```
your-project/
└── .nexus/               # Cloned codex-test repository
    └── pkg/
        ├── akads/        # Same structure as development mode
        └── utils/        # Same structure as development mode
```

## Usage Notes

1. The JSON structure file must be valid and accessible
2. The command module must exist and have a valid `run` function
3. Default mode is "prod" when no mode is specified
4. Core implementation is in run.py, using shared utilities
5. Built-in documentation commands are in run_docs.py
6. Path handling is managed by utils/get_base_path.py
7. Production mode requires codex-test to be cloned as .nexus in the target repository

## Example JSON Structure

```json
{
  "files": [
    {
      "name": "Button",
      "path": "src/components/Button",
      "type": "component",
      "content": "..."
    },
    {
      "name": "styles",
      "path": "src/styles/button.css",
      "type": "style",
      "content": "..."
    },
    {
      "name": "utils",
      "path": "src/utils/helpers.js",
      "type": "utility",
      "content": "..."
    }
  ]
}
