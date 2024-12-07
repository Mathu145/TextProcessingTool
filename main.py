from core.core import Core

core = Core()
text = core.read_file("test.txt")
core.write_file("output.txt", text)

from core.core import Core

core = Core()
core.load_plugins()
print("Text Processing Tool")
file_path = input("Enter the path of the text file: ")
text = core.read_file(file_path)

while True:
    print("\n--- Menu ---")
    core.show_plugins()
    print("0 - Exit")
    choice = input("Choose a plugin: ")

    if choice == "0":
        break
    elif choice in core.plugins:
        text = core.apply_plugin(choice, text)
        print("\nProcessed Text:")
        print(text)
    else:
        print("Invalid choice.")

save_path = input("Enter the path to save the processed text: ")
core.write_file(save_path, text)