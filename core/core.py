import os

class Core:
    """
    Core module for handling plugins and basic text processing functionality.
    """

    def __init__(self):
        # Dictionary to store dynamically loaded plugins
        self.plugins = {}

    def load_plugins(self):
        """
        Dynamically loads plugins from the 'plugins' directory.
        Each plugin must follow the naming convention <plugin_name>.py and define a class 'Plugin'.
        """
        plugin_dir = os.path.join(os.path.dirname(__file__), "../plugins")
        for filename in os.listdir(plugin_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                plugin_name = filename[:-3]
                try:
                    # Dynamically import the plugin
                    module = __import__(f"plugins.{plugin_name}", fromlist=["Plugin"])
                    plugin_class = getattr(module, "Plugin")
                    self.plugins[plugin_name] = plugin_class()
                except Exception as e:
                    print(f"Error loading plugin '{plugin_name}': {e}")

    def show_plugins(self):
        """
        Displays all available plugins to the user.
        """
        print("Available Plugins:")
        for name in self.plugins.keys():
            print(f"- {name}")

    def apply_plugin(self, plugin_name, text):
        """
        Applies the selected plugin to the given text.
        """
        if plugin_name in self.plugins:
            return self.plugins[plugin_name].process(text)
        else:
            print(f"Plugin '{plugin_name}' not found.")
            return text
    def read_file(self, file_path):
        """
        Reads text from a given file path.
        """
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()
        except Exception as e:
            print(f"Error reading file: {e}")
            return ""

    def write_file(self, file_path, text):
        """
        Writes text to a specified file path.
        """
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text)
                print(f"Text successfully saved to {file_path}")
        except Exception as e:
            print(f"Error writing file: {e}")