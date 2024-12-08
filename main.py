from core.core import Core

def main():
    core = Core()
    core.load_plugins()

    print("Welcome to the Text Processing Tool")
    file_path = input("Enter the path of the text file to process: ")
    text = core.read_file(file_path)

    while True:
        print("\n--- Menu ---")
        core.show_plugins()
        print("0 - Exit")
        choice = input("Choose a plugin (or 0 to exit): ")

        if choice == "0":
            break
        elif choice in core.plugins:
            text = core.apply_plugin(choice, text)
            print("\nProcessed Text:")
            print(text)
        else:
            print("Invalid choice. Please try again.")

    save_path = input("Enter the path to save the processed text: ")
    core.write_file(save_path, text)

if __name__ == "__main__":
    main()
