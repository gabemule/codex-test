# 📚 Documentation Generator

This module runs documentation generation based on a JSON structure file. The documentation generator automatically detects if it's running from:
- **🔧 Development**: When running directly from the project root
- **🚀 Production**: When running from another project with .codex/

## 📋 Usage Patterns

### 💻 Command-line Usage (via __main__.py)

```bash
# Add project root to PYTHONPATH first
export PYTHONPATH=$PWD
# or
export PYTHONPATH=$PWD/.codex

# Generate documentation
python -m pkg.akads --json-path .tmp/tree_project.json
```

### 🔧 Programmatic Usage (via __init__.py)

```python
from pkg.akads import run
run(json_path=".tmp/tree_project.json")
```

## 🚀 Complete Workflows

### 🔧 Development Mode

When working directly in the project root:

```bash
# 1. Activate virtual environment (only needed once)
source bin/start.sh

# 2. Generate project tree (needed before documentation generation)
./bin/tree_generate_all.sh

# 3. Set your Anthropic API key (required for documentation generation)
export ANTHROPIC_API_KEY=your_api_key_here

# 4. Add project root to PYTHONPATH
export PYTHONPATH=$PWD

# 5. Install aider (only needed once)
python -m shared.require_aider

# 6. Generate documentation
python -m pkg.akads  # Command-line usage
# or
python3 -c "from pkg.akads import run; run()"  # Programmatic usage
```

### 🚀 Production Mode

When using as a tool in another repository:

```bash
# 1. Clone codex as .codex
git clone https://github.com/your-org/codex.git .codex

# 2. Activate virtual environment (only needed once)
source .codex/bin/start.sh

# 3. Generate project tree (needed before documentation generation)
./.codex/bin/tree_generate_all.sh

# 4. Set your Anthropic API key (required for documentation generation)
export ANTHROPIC_API_KEY=your_api_key_here

# 5. Add .codex to PYTHONPATH
export PYTHONPATH=$PWD/.codex

# 6. Install aider (only needed once)
python -m shared.require_aider

# 7. Generate documentation
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

## 🔄 Path Handling

The module uses `utils/get_base_path.py` to handle paths correctly based on the environment:

```python
from utils.get_base_path import get_base_path

base = get_base_path()  # Returns "." or ".codex" based on environment
```

This ensures that files (like prompts and templates) are accessed from the correct location:
- When in project root: Files are loaded from `./...`
- When in another project: Files are loaded from `.codex/...`

## 📁 Directory Structure

### 🔧 Development Mode (in project root)
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
├── get_base_path.py       # Path handling with environment detection
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

1. ✨ Virtual environment activation and aider installation only need to be done once
2. 🔄 Project tree must be generated before documentation generation
3. 🔑 The ANTHROPIC_API_KEY must be set before running pkg.akads
4. 🛠️ Core implementation is in run.py, using shared utilities
5. 🔧 Path handling is managed by utils/get_base_path.py with automatic environment detection
6. 📦 Production mode requires:
   - codex to be cloned as .codex in the target repository
   - .codex to be added to PYTHONPATH
