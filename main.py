from core.core import Core

core = Core()
text = core.read_file("test.txt")
core.write_file("output.txt", text)
