import re

class Plugin:
    """
    Searches for a specific keyword, character, or number in the text,
    highlights occurrences, and displays the total count of matches at the end.
    """

    def process(self, text):
        if not text.strip():
            return "The input text is empty. Please provide valid text."

        # Prompt the user for the keyword to search
        keyword = input("Enter the keyword, character, or number to search: ").strip()

        if not keyword:
            return "No keyword entered. Please try again."

        # Escape special characters in the keyword for regex search
        escaped_keyword = re.escape(keyword)

        # Search for the keyword and count occurrences (case-insensitive)
        matches = re.findall(escaped_keyword, text, re.IGNORECASE)
        count = len(matches)

        if count == 0:
            return f"The keyword, character, or number '{keyword}' was not found in the text."

        # Highlight the keyword with noticeable markers (case-insensitive replace)
        highlighted_text = re.sub(
            escaped_keyword, f"***{keyword.upper()}***", text, flags=re.IGNORECASE
        )

        # Return the modified text along with the summary at the end
        return (
            f"{highlighted_text}\n\n"
            f"***************************************************************************************\n"
            f"The keyword, character, or number '{keyword}' was found {count} time(s) in the text.\n"
            f"Highlighted with ***UPPERCASE*** to make it easily noticeable.\n"
            f"***************************************************************************************"
        )