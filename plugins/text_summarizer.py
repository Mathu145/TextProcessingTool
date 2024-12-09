class Plugin:
    """
    Provides a summary by extracting sentences that contain key terms.
    """
    def process(self, text):
        # Define important keywords to look for
        keywords = ["important", "summary", "key", "focus", "highlight", "critical", "essential"]

        # Split the text into sentences. Use both "." and "\n" for sentence separation.
        sentences = text.replace("\n", " ").split(".")
        summary = []

        # Check each sentence for keywords
        for sentence in sentences:
            if any(keyword in sentence.lower() for keyword in keywords):
                summary.append(sentence.strip())

        # Return the summary or a default message if no keywords found
        if summary:
            return "Summary:\n" + ". ".join(summary) + "."
        else:
            return "No significant sentences with keywords found in the text."