"""
Extractor module
"""

from .api import API


class Extractor(API):
    """
    Extractor instance.
    """

    def extract(self, queue, texts=None):
        """
        Extracts answers to input questions.

        Args:
            queue: list of {name: value, query: value, question: value, snippet: value}
            texts: optional list of text

        Returns:
            list of {name: value, answer: value}
        """

        return self.execute("post", "extract", {"queue": queue, "texts": texts})
