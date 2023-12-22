"""
Segmentation module
"""

from .api import API


class Segmentation(API):
    """
    Segmentation instance.
    """

    def segment(self, text):
        """
        Segments text into semantic units.

        Args:
            text: input text

        Returns:
            segmented text
        """

        return self.execute("get", "segment", {"text": text})

    def batchsegment(self, texts):
        """
        Segments text into semantic units.

        Args:
            texts: list of texts to segment

        Returns:
            list of segmented text
        """

        return self.execute("post", "batchsegment", {"texts": texts})
