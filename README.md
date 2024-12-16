# Text Processing Tool

## Overview
A text processing tool built using the Microkernel architecture. This tool allows users to dynamically load plugins and perform various text processing tasks on selected text files, providing a flexible and extensible solution for text analysis.

## Plugins
1. **Word Counter**: Counts the number of words in the text while ignoring punctuation.
2. **Case Converter**: Converts the text to uppercase, lowercase, or capitalizes each word.
3. **Text Search**: Searches for a specific keyword, highlights its occurrences, and displays the total count.
4. **Sentiment Analysis**: Analyzes the sentiment of the text and classifies it as positive, negative, or neutral. It also lists positive and negative words found in the text.
5. **Text Summarizer**: Extracts sentences containing predefined or user-defined keywords to provide a concise summary of the text.

## Prerequisites
1. **Python Installation**: Ensure Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/).
2. **Verify Installation**: After installing Python, verify it using:
   ```bash
   python --version

or

python3 --version

3. **Install Missing Components**: If any required Python components are missing, you may need to install them. For example:
Open a terminal or command prompt.
Run the following command to install the necessary standard libraries (if not already included):

pip install --upgrade pip

## How to Run
1. Place your text file in the project directory (the same folder as main.py) or provide the full file path (including the file name and suffix, e.g., example.txt) during the file selection process.
2. Execute the application using one of the following commands:<br>
   
   **python main.py**
   
   or
   
   **python3 main.py**

3. Follow the on-screen prompts to::
- Choose how to select your file:
   - Option 1: Select from available text files in the current directory.
   - Option 2: Enter the full path to your text file manually (must include the file name and suffix, e.g., C:/path/to/your/file.txt).
- Select a plugin from the dynamically loaded list.
- View the processed text.
- Optionally save the processed text to a new file.

## Structure
- core/: Contains the core system (core.py) responsible for managing plugins, reading files, and applying plugins.
- plugins/: Contains modular plugin implementations, each designed to perform a specific text processing task.
- main.py: The entry point for the application, responsible for managing user interaction and coordinating tasks.

## Requirements
- Python 3.x
- No external dependencies are required. If any issues arise, ensure that Python is installed and updated.

## Adding New Plugins
1. Create a new Python file in the plugins/ directory.
2. Define a Plugin class with a process(self, text) method.
3. Implement your custom text processing logic within the process method.
4. The system will automatically detect and load your plugin the next time it runs.