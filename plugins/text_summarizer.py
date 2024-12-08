class Plugin:
    """
    Provides a summary of the text by extracting sentences with key terms.
    """

    def process(self, text):
        keywords = ["important", "summary", "key", "focus", "highlight"]
        sentences = text.split(".")
        summary = [
            sentence.strip() + "."
            for sentence in sentences
            if any(keyword in sentence.lower() for keyword in keywords)
        ]

        if summary:
            return " ".join(summary)
        else:
            return "No significant summary available."
