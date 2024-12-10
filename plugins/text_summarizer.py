import re

class Plugin:
    """
    Provides a summary by extracting sentences that contain key terms.
    """
    def process(self, text):
        if not text.strip():
            return "The input text is empty. Please provide valid text."

        # Predefined important keywords
        default_keywords = ["important", "summary", "key", "focus", "highlight", "critical", "essential"]

        # Inform the user about predefined keywords
        print(f"Default keywords: {', '.join(default_keywords)}")

        # Allow user to add custom keywords
        user_keywords = input(
            "Enter additional keywords to search for (comma-separated) or press Enter to use defaults: "
        ).strip()

        # Combine predefined and user-provided keywords
        if user_keywords:
            keywords = default_keywords + [kw.strip().lower() for kw in user_keywords.split(",")]
        else:
            keywords = default_keywords

        print(f"\nUsing the following keywords for summarization: {', '.join(keywords)}")

        # Split text into sentences
        sentences = re.split(r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", text.replace("\n", " "))
        summary = [sentence.strip() for sentence in sentences if any(keyword in sentence.lower() for keyword in keywords)]

        # Return the summary or a default message
        return "Summary:\n" + " ".join(summary) if summary else "No significant sentences with the specified keywords were found in the text."