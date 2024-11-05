# 📦 Packages

This directory contains reusable packages that provide various functionalities for the project. Each package is designed to be used either as a module or programmatically, with automatic environment detection.

## 🎯 Available Packages

### 📚 akads
Documentation generation for React and Sass components.
- 🔄 Processes React components, stories, and TypeScript files
- 🎨 Processes Sass styles and components
- 🛠️ Supports both module and programmatic usage
- 📖 [Technical Documentation](akads/README.md)

### 📝 changelog
Changelog generation from git commits.
- ✨ Generates formatted changelogs using aider
- 📋 Supports multiple sections (Added, Changed, Fixed, etc.)
- 🏷️ Handles breaking changes and version tags
- 📖 [Technical Documentation](changelog/README.md)

## ⭐ Common Features

All packages share common characteristics:
- **🔄 Environment Detection**: Automatically detects if running from project root or .codex
- **🔧 Flexible Usage**: Can be used as a module or imported programmatically
- **🔍 Error Handling**: Comprehensive error handling and reporting
- **📂 Path Resolution**: Automatic path handling for different environments

## 📋 Usage Patterns

### 💻 Module Usage
```bash
# From project root
export PYTHONPATH=$PWD
python -m pkg.<package_name> [options]

# From another project
export PYTHONPATH=/path/to/project/.codex
python -m pkg.<package_name> [options]
```

### 🔧 Programmatic Usage
```python
# From project root
export PYTHONPATH=$PWD
from pkg.<package_name> import run
run(**options)

# From another project
export PYTHONPATH=/path/to/project/.codex
from pkg.<package_name> import run
run(**options)
```

## 📁 Directory Structure

```
pkg/
├── README.md          # This file
├── akads/             # Documentation generator
│   ├── __init__.py
│   ├── __main__.py
│   ├── run.py
│   └── README.md
└── changelog/         # Changelog generator
    ├── __init__.py
    ├── __main__.py
    ├── run.py
    └── README.md
```

## 🚀 Development

When creating new packages:
1. Follow the established package structure
2. Support both module and programmatic usage
3. Use automatic environment detection
4. Provide comprehensive documentation
5. Include usage examples

## 📋 Package Guidelines

Each package should:
- 🎯 Have a clear, single responsibility
- 🔄 Support automatic environment detection
- 📚 Include comprehensive documentation
- 🖥️ Provide both CLI and programmatic interfaces
- ⚠️ Handle errors gracefully
- 🛠️ Use shared utilities when appropriate

## 🌍 Environment Detection

The environment is automatically detected:
- **🔧 Project Root**: When running directly from the repository
  - Has pkg/ and utils/ directories
  - Uses local paths ("./")
  - Helpful for package development and testing

- **🚀 Another Project**: When running from .codex in another repository
  - Has .codex/ directory
  - Uses .codex-prefixed paths
  - Default for end users

## 🛠️ Utilities

Packages can use shared utilities from the utils/ directory:
- `🔍 get_base_path`: Automatic environment detection and path resolution
- `📄 load_json`: JSON file loading and parsing
- `📝 load_template`: Template processing

For utility documentation, see [utils/README.md](../utils/README.md)

## 🤝 Contributing

When adding a new package:
1. Create a new directory in pkg/
2. Follow the established package structure
3. Implement both usage patterns (module/programmatic)
4. Add comprehensive documentation
5. Update this README.md
