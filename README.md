# Text Processing Tool

## Overview
A text processing tool built using the Microkernel architecture. This tool dynamically loads plugins to perform various text processing tasks on user-selected text files.

## Plugins
1. **Word Counter**: Counts the number of words in the text.
2. **Case Converter**: Converts the text to uppercase, lowercase, or capitalizes each word.
3. **Text Search**: Searches for a keyword, highlights occurrences, and displays the total count of matches.
4. **Sentiment Analysis**: Analyzes the text to determine whether the sentiment is positive, neutral, or negative based on predefined word lists.
5. **Text Summarizer**: Extracts sentences containing key terms to provide a concise summary of the text.

## How to Run
1. Ensure your text file is in the project directory or provide the full path to the file during the file selection process.
2. Run the application by executing the following command:\n
   
   **python main.py**
   
   or
   
   **python3 main.py**

3. Follow the prompts to:
- Select a text file.
- Choose a plugin to apply.
- View the processed text.
- Optionally save the processed text to a new file.

## Structure
- core/:        #Contains the core system.
- plugins/:     #Contains individual plugins.
- main.py:      #Entry point for the application.

## Requirements
- Python 3.x
- No additional dependencies are required.

## Adding New Plugins
1. Create a new Python file in the plugins/ directory.
2. Define a Plugin class with a process(self, text) method.
3. Implement your custom text processing logic in the process method.
4. The tool will automatically detect and load your new plugin the next time it runs.

## Notes
- The tool gracefully handles empty or invalid text files by providing appropriate messages.
- Plugins are modular and can be dynamically added or removed without altering the core system.
