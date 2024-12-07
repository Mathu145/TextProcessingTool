# Text Processing Tool

## Overview
A simple text processing tool using the microkernel architecture.

## Features
- Core functionality for reading, processing, and saving text files.
- Plugin support for extended functionality:
  - Word Counter: Counts the number of words in the text.
  - Case Converter: Converts text to uppercase.
  - Text Search: Searches for and counts occurrences of a keyword.

## Usage
1. Run `main.py`.
2. Provide the path to a text file.
3. Select a plugin to process the text.
4. Save the processed text to a new file.

## Structure
- `core/`: Contains the core system.
- `plugins/`: Contains individual plugins.
- `main.py`: Entry point for the application.
