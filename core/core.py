import os
import importlib.util

class Core:
    """
    The Core class manages plugins and handles text processing tasks.
    """

    def __init__(self):
        self.plugins = {}

    def load_plugins(self):
        """
        Dynamically loads plugins from the 'plugins' directory without relying on __init__.py.
        """
        plugin_directory = os.path.join(os.path.dirname(__file__), "../plugins")
        for file in os.listdir(plugin_directory):
            if file.endswith(".py") and file != "__init__.py":
                plugin_name = file[:-3]
                plugin_path = os.path.join(plugin_directory, file)
                try:
                    # Dynamically load the plugin module
                    spec = importlib.util.spec_from_file_location(plugin_name, plugin_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    
                    # Load the Plugin class
                    plugin_class = getattr(module, "Plugin")
                    self.plugins[plugin_name] = plugin_class()
                except Exception as error:
                    print(f"Error loading plugin '{plugin_name}': {error}")

    def list_plugins(self):
        """
        Lists all available plugins with numbering.
        """
        print("Available Plugins:")
        for i, plugin_name in enumerate(self.plugins, start=1):
            print(f"{i}. {plugin_name}")

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
        Reads text from a file and warns if the file is empty.
        """
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                if not content.strip():
                    print("The file is empty.")
                    return ""
                return content
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
                print(f"Text successfully saved to {file_path}.")
        except Exception as error:
            print(f"Error writing file: {error}")