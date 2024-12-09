class Plugin:
    """
    Converts text to uppercase, lowercase, or capitalizes each word.
    Allows the user to return to the main menu by entering 0.
    """
    def process(self, text):
        while True:
            print("\nChoose an option for case conversion:")
            print("1 - Convert to UPPERCASE")
            print("2 - Convert to lowercase")
            print("3 - Capitalize Each Word")
            print("0 - Return to the main menu")

            try:
                # Prompt the user for a choice
                choice = int(input("Enter your choice (0, 1, 2, or 3): ").strip())
                
                if choice == 0:
                    print("Returning to the main menu...")
                    return text  # No change, returns to the main menu
                
                elif choice == 1:
                    print("Converting text to UPPERCASE...")
                    return text.upper()
                
                elif choice == 2:
                    print("Converting text to lowercase...")
                    return text.lower()
                
                elif choice == 3:
                    print("Capitalizing each word...")
                    return text.title()
                
                else:
                    print("Invalid choice. Please enter a number between 0 and 3.")
            
            except ValueError:
                print("Invalid input. Please enter a valid number (0, 1, 2, or 3).")