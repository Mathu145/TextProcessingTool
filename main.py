from core.core import Core

# Initialize the core system
core = Core()
core.load_plugins()

# Display welcome message
print("Welcome to the Text Processing Tool")

# Prompt the user to enter a file path
file_path = input("Enter the path of the text file: ")
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

# Save the processed text
save_path = input("Enter the path to save the processed text: ")
core.write_file(save_path, text)
