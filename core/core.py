import os

class Core:
    def __init__(self):
        self.plugins = {}

    def load_plugins(self):
        plugin_dir = os.path.join(os.path.dirname(__file__), "../plugins")
        for filename in os.listdir(plugin_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                plugin_name = filename[:-3]
                try:
                    module = __import__(f"plugins.{plugin_name}", fromlist=["Plugin"])
                    plugin_class = getattr(module, "Plugin")
                    self.plugins[plugin_name] = plugin_class()
                except Exception as e:
                    print(f"Fehler beim Laden von {plugin_name}: {e}")

    def show_plugins(self):
        print("Verfügbare Plugins:")
        for name in self.plugins.keys():
            print(f"- {name}")

    def apply_plugin(self, plugin_name, text):
        if plugin_name in self.plugins:
            return self.plugins[plugin_name].process(text)
        else:
            print(f"Plugin '{plugin_name}' nicht gefunden.")
            return text
class Core:
    # (Bestehender Code bleibt gleich)

    def read_file(self, file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()
        except Exception as e:
            print(f"Fehler beim Lesen der Datei: {e}")
            return ""

    def write_file(self, file_path, text):
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(text)
                print(f"Text erfolgreich in {file_path} gespeichert.")
        except Exception as e:
            print(f"Fehler beim Speichern der Datei: {e}")
