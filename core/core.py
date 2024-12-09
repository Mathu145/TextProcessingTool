import os

class Core:
    """
    The Core class manages plugins and handles text processing tasks.
    """

    def __init__(self):
        self.plugins = {}

    def load_plugins(self):
        """
        Dynamically loads plugins from the 'plugins' directory.
        """
        plugin_directory = os.path.join(os.path.dirname(__file__), "../plugins")
        for file in os.listdir(plugin_directory):
            if file.endswith(".py") and file != "__init__.py":
                plugin_name = file[:-3]
                try:
                    module = __import__(f"plugins.{plugin_name}", fromlist=["Plugin"])
                    plugin_class = getattr(module, "Plugin")
                    self.plugins[plugin_name] = plugin_class()
                except Exception as error:
                    print(f"Error loading plugin '{plugin_name}': {error}")

    def list_plugins(self):
        """
        Lists all available plugins.
        """
        print("Available Plugins:")
        for plugin_name in self.plugins:
            print(f"- {plugin_name}")

    def apply_plugin(self, plugin_name, text):
        """
        Applies the selected plugin to the text.
        """
        if plugin_name in self.plugins:
            plugin = self.plugins[plugin_name]
            return plugin.process(text)
        else:
            print(f"Plugin '{plugin_name}' not found.")
            return text

    def read_file(self, file_path):
        """
        Reads text from a file.
        """
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()
        except FileNotFoundError:
            print("File not found.")
            return ""
        except Exception as error:
            print(f"Error reading file: {error}")
            return ""

    def write_file(self, file_path, content):
        """
        Writes text to a file.
        """
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)
                print(f"Text saved to {file_path}.")
        except Exception as error:
            print(f"Error writing file: {error}")