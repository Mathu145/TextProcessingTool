class Plugin:
    def process(self, text):
        words = text.split()
        return f"Word count: {len(words)}"
