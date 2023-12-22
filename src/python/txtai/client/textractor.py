"""
Textractor module
"""

from .api import API


class Textractor(API):
    """
    Textractor instance.
    """

    def textract(self, file):
        """
        Extracts text from a file at path.

        Args:
            file: file to extract text

        Returns:
            extracted text
        """

        return self.execute("get", "textract", {"file": file})

    def batchtextract(self, files):
        """
        Extracts text from a file at path.

        Args:
            files: list of files to extract text

        Returns:
            list of extracted text
        """

        return self.execute("post", "batchtextract", files)
