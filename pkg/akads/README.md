# 📚 Documentation Generator

This module runs documentation generation based on a JSON structure file. The documentation generator can be used in two modes:
- **🔧 dev**: Running directly from the codex repository
- **🚀 prod**: Running from .codex/pkg when codex is cloned as .codex in another repository

## 📋 Usage Patterns

### 💻 Command-line Usage (via __main__.py)

Development mode (in codex repository):
```bash
python -m pkg.akads --mode dev --json-path .tmp/tree_project.json
```

Production mode (in repository with .codex):
```bash
# Add .codex to PYTHONPATH first
PYTHONPATH=/path/to/project/.codex python -m pkg.akads --json-path .tmp/tree_project.json
# or
export PYTHONPATH=/path/to/project/.codex
python -m pkg.akads --json-path .tmp/tree_project.json
```

### 🔧 Programmatic Usage (via __init__.py)

Development mode (in codex repository):
```python
from pkg.akads import run
run(json_path=".tmp/tree_project.json", mode="dev")
```

Production mode (in repository with .codex):
```python
import sys
sys.path.append('/path/to/project/.codex')  # Add .codex to Python path
from pkg.akads import run
run(json_path=".tmp/tree_project.json")  # mode defaults to "prod"
```

## 🚀 Complete Workflows

### 🔧 Development Mode

When working directly in the codex repository:

```bash
# 1. Activate virtual environment (only needed once)
source bin/start.sh --mode dev

# 2. Generate project tree (needed before documentation generation)
./bin/tree_generate_all.sh

# 3. Install aider-chat (only needed once)
python shared/require_aider-chat.py

# 4. Set your Anthropic API key (required for documentation generation)
export ANTHROPIC_API_KEY=your_api_key_here

# 5. Generate documentation (choose one):
python -m pkg.akads --mode dev  # Command-line usage
# or
python3 -c "from pkg.akads import run; run(mode='dev')"  # Programmatic usage
```

### 🚀 Production Mode

When using codex as a tool in another repository:

```bash
# 1. Clone codex as .codex
git clone https://github.com/your-org/codex.git .codex

# 2. Activate virtual environment (only needed once)
source .codex/bin/start.sh

# 3. Generate project tree (needed before documentation generation)
./.codex/bin/tree_generate_all.sh

# 4. Install aider-chat (only needed once)
python .codex/shared/require_aider-chat.py

# 5. Set your Anthropic API key (required for documentation generation)
export ANTHROPIC_API_KEY=your_api_key_here

# 6. Add .codex to PYTHONPATH
export PYTHONPATH=$PWD/.codex

# 7. Generate documentation (choose one):
python -m pkg.akads  # Command-line usage
# or
python3 -c "from pkg.akads import run; run()"  # Programmatic usage

# 8. Optional: Clean up when done
rm -rf .codex
```

## 📚 Documentation Modules

The package includes specialized modules for different types of documentation:

### ⚛️ React Documentation (run_doc_react.py)
Processes React components and generates documentation for:
- 📖 Story files (.stories.tsx)
- 🔧 Component files (.tsx with .config.ts)
- 📝 TypeScript utility files

### 🎨 Sass Documentation (run_doc_sass.py)
Processes Sass files and generates documentation for:
- 🎯 SCSS files
- 🔧 Style components
- 🛠️ Functions and mixins

## ⚙️ Parameters

- **📄 json_path**: Path to the JSON file containing the project structure
  - Default: `.tmp/tree_project.json`
  - The JSON file should contain the project structure to be processed

- **🔧 mode**: Running mode, either "prod" or "dev"
  - Default: "prod"
  - "prod": Running from .codex in another repository
  - "dev": Running directly from codex repository

## 🔄 Path Handling

The module uses `utils/get_base_path.py` to handle paths correctly in both production and development modes:

```python
from utils.get_base_path import get_base_path

base = get_base_path(mode)  # Returns ".codex" for prod, "." for dev
```

This ensures that files (like prompts and templates) are accessed from the correct location:
- In production mode (default): Files are loaded from `.codex/...`
- In development mode: Files are loaded from `./...`

## 📁 Directory Structure

### 🔧 Development Mode (in codex repository)
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

### 🚀 Production Mode (in another repository)
```
your-project/
└── .codex/               # Cloned codex repository
    └── pkg/
        ├── akads/        # Same structure as development mode
        └── utils/        # Same structure as development mode
```

## 📝 Usage Notes

1. ✨ Virtual environment activation and aider-chat installation only need to be done once
2. 🔄 Project tree must be generated before documentation generation
3. 🔑 The ANTHROPIC_API_KEY must be set before running pkg.akads
4. 🚀 Default mode is "prod" when no mode is specified
5. 🛠️ Core implementation is in run.py, using shared utilities
6. 🔧 Path handling is managed by utils/get_base_path.py
7. 📦 Production mode requires:
   - codex to be cloned as .codex in the target repository
   - .codex to be added to PYTHONPATH
