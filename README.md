[README.md](https://github.com/user-attachments/files/26331570/README.md)
# File Sorter

A simple Python utility that organizes mixed file types into extension-based folders.

## Features

- Automatic file sorting
- Extension-based organization
- Creates folders automatically
- Simple and fast utility

## Project Structure

FileSorter/
│── .gitignore                 # Git ignore rules
│── TODO.md                    # Future improvements
│── file_sorter.py             # Main entry point
│── requirements.txt           # Dependencies
│
├── config/
│   └── __init__.py            # Config package
│
├── core/
│   ├── __init__.py            # Core initializer
│   │
│   ├── compression/
│   │   └── __init__.py
│   │
│   ├── converters/
│   │   └── __init__.py
│   │
│   └── file_ops/
│       └── __init__.py        # Sorting logic
│
├── ui/
│   └── __init__.py            # UI helpers
│
├── utils/
│   └── __init__.py            # Utility functions
│
└── tests/
    └── __init__.py            # Test package

## Requirements

```bash
pip install -r requirements.txt
```
