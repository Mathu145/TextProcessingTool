class Plugin:
    """
    Counts the number of words in a given text.
    """
    def process(self, text):
        word_count = len(text.split())
        return f"Word count: {word_count}"