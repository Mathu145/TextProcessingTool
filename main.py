import os
from core.core import Core

def list_items(items, item_type="option"):
    """
    Dynamically display a numbered list of items (files, plugins, etc.).
    """
    print(f"\nAvailable {item_type}s:")
    for i, item in enumerate(items, start=1):
        print(f"{i} - {item}")
    print("0 - Exit")
    return items

def choose_item(items, item_type="option"):
    """
    Allow the user to select an item from a numbered list.
    """
    while True:
        try:
            choice = int(input(f"Choose a {item_type} by number (or enter 0 to exit): ").strip())
            if choice == 0:
                return None
            elif 1 <= choice <= len(items):
                return items[choice - 1]
            else:
                print(f"Invalid choice. Please enter a number between 1 and {len(items)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    """
    Main function to manage text processing using a microkernel architecture.
    """
    # List text files in the current directory
    text_files = [file for file in os.listdir('.') if file.endswith('.txt')]
    print("\nHow would you like to select your file?")
    print("1 - Choose from available text files in the current directory")
    print("2 - Enter the full file path manually")
    print("0 - Exit")

    try:
        file_choice = int(input("Enter your choice (0, 1, or 2): ").strip())
        if file_choice == 0:
            print("Exiting the program.")
            return
        elif file_choice == 1:
            if not text_files:
                print("No text files found in the current directory.")
                return
            list_items(text_files, "text file")
            file_path = choose_item(text_files, "text file")
        elif file_choice == 2:
            file_path = input("Enter the full path to your text file: ").strip()
        else:
            print("Invalid choice. Exiting.")
            return
    except ValueError:
        print("Invalid input. Exiting.")
        return

    if not file_path:
        print("No file selected. Exiting.")
        return

    # Initialize Core and load plugins
    core = Core()
    core.load_plugins()

    print(f"\nSelected file: {file_path}")
    text = core.read_file(file_path)

    if not text:
        print("The selected file is empty or could not be read. Exiting.")
        return

    while True:
        # Display available plugins
        plugins_list = list(core.plugins.keys())
        list_items(plugins_list, "plugin")
        selected_plugin = choose_item(plugins_list, "plugin")
        if not selected_plugin:
            print("Exiting the program.")
            break

        print(f"\nApplying plugin: {selected_plugin}")
        # Process the text with the selected plugin
        processed_text = core.apply_plugin(selected_plugin, text)
        print("\nProcessed Text:")
        print(processed_text)

        # Ask user if they want to save the processed text
        save_choice = input("\nDo you want to save the processed text? (y/n): ").strip().lower()
        if save_choice == 'y':
            output_file = input("Enter the name of the output file (default: output.txt): ").strip()
            if not output_file:
                output_file = "output.txt"
            core.write_file(output_file, processed_text)
            print(f"Processed text saved to {output_file}.")
        else:
            print("Processed text was not saved.")

if __name__ == "__main__":
    main()