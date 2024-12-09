import re

class Plugin:
    """
    Provides a summary by extracting sentences that contain key terms.
    """
    def process(self, text):
        if not text.strip():
            return "The input text is empty. Please provide valid text."

        # Define default important keywords to look for
        default_keywords = ["important", "summary", "key", "focus", "highlight", "critical", "essential"]

        # Allow user to add custom keywords
        user_keywords = input(
            "Enter additional keywords to search for (comma-separated) or press Enter to use defaults: "
        ).strip()

        # Combine default and user-provided keywords
        if user_keywords:
            keywords = default_keywords + [kw.strip().lower() for kw in user_keywords.split(",")]
        else:
            keywords = default_keywords

        print(f"\nUsing the following keywords for summarization: {', '.join(keywords)}\n")

        # Split the text into sentences using regex
        sentences = re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", text.replace("\n", " "))
        summary = []

        # Check each sentence for keywords
        for sentence in sentences:
            if any(keyword in sentence.lower() for keyword in keywords):
                summary.append(sentence.strip())

        # Return the summary or a default message if no keywords are found
        if summary:
            return "Summary:\n" + " ".join(summary)
        else:
            return "No significant sentences with the specified keywords were found in the text."