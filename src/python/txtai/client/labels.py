"""
Labels module
"""

from .api import API


class Labels(API):
    """
    Labels instance.
    """

    def label(self, text, labels):
        """
        Applies a zero shot classifier to text using a list of labels. Returns a list of
        {id: value, score: value} sorted by highest score, where id is the index in labels.

        Args:
            text: input text
            labels: list of labels

        Returns:
            list of {id: value, score: value} per text element
        """

        return self.execute("post", "label", {"text": text, "labels": labels})

    def batchlabel(self, texts, labels):
        """
        Applies a zero shot classifier to list of text using a list of labels. Returns a list of
        {id: value, score: value} sorted by highest score, where id is the index in labels per
        text element.

        Args:
            texts: list of text
            labels: list of labels

        Returns:
            list of {id: value score: value} per text element
        """

        return self.execute("post", "batchlabel", {"texts": texts, "labels": labels})
