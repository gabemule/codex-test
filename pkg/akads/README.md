# Documentation Generator

This module runs documentation generation based on a JSON structure file. The documentation generator can be used in two modes:
- **dev**: Running directly from the codex-test repository
- **prod**: Running from .nexus/pkg when codex-test is cloned as .nexus in another repository

## Usage Patterns

### Command-line Usage (via __main__.py)

Development mode (in codex-test repository):
```bash
python -m pkg.akads --mode dev --json-path .tmp/tree_project.json
```

Production mode (in repository with .nexus):
```bash
python -m pkg.akads --json-path .tmp/tree_project.json  # mode defaults to "prod"
```

### Programmatic Usage (via __init__.py)

Development mode (in codex-test repository):
```python
from pkg.akads import run
run(json_path=".tmp/tree_project.json", mode="dev")
```

Production mode (in repository with .nexus):
```python
from .nexus.pkg.akads import run
run(json_path=".tmp/tree_project.json")  # mode defaults to "prod"
```

## Documentation Modules

The package includes specialized modules for different types of documentation:

### React Documentation (run_doc_react.py)
Processes React components and generates documentation for:
- Story files (.stories.tsx)
- Component files (.tsx with .config.ts)
- TypeScript utility files

### Sass Documentation (run_doc_sass.py)
Processes Sass files and generates documentation for:
- SCSS files
- Style components
- Functions and mixins

## Parameters

- **json_path**: Path to the JSON file containing the project structure
  - Default: `.tmp/tree_project.json`
  - The JSON file should contain the project structure to be processed

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

This ensures that files (like prompts and templates) are accessed from the correct location:
- In production mode (default): Files are loaded from `.nexus/...`
- In development mode: Files are loaded from `./...`

## Directory Structure

### Development Mode (in codex-test repository)
```
pkg/
└── akads/
    ├── __init__.py          # Handles programmatic usage exports
    ├── __main__.py         # Handles command-line interface
    ├── run.py              # Core implementation
    ├── run_doc_react.py   # React documentation implementation
    ├── run_doc_sass.py    # Sass documentation implementation
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
2. The module automatically detects and processes React and Sass structures
3. Default mode is "prod" when no mode is specified
4. Core implementation is in run.py, using shared utilities
5. Path handling is managed by utils/get_base_path.py
6. Production mode requires codex-test to be cloned as .nexus in the target repository

## Example JSON Structure

```json
{
  "react": {
    "src": {
      "components": {
        "atoms": {
          "Button": {
            "files": [
              "Button.tsx",
              "Button.stories.tsx",
              "Button.config.ts"
            ]
          }
        }
      }
    }
  },
  "sass": {
    "src": {
      "components": {
        "atoms": {
          "Button": {
            "files": [
              "Button.scss"
            ]
          }
        }
      }
    }
  }
}
