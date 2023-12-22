"""
Summary module
"""

from .api import API


class Summary(API):
    """
    Summary instance.
    """

    def summary(self, text, minlength=None, maxlength=None):
        """
        Runs a summarization model against a block of text.

        Args:
            text: text to summarize
            minlength: minimum length for summary
            maxlength: maximum length for summary

        Returns:
            summary text
        """

        params = {"text": text}
        if minlength:
            params["minlength"] = minlength
        if maxlength:
            params["maxlength"] = maxlength

        return self.execute("get", "summary", params)

    def batchsimilarity(self, texts, minlength=None, maxlength=None):
        """
        Runs a summarization model against a block of text.

        Args:
            texts: list of text to summarize
            minlength: minimum length for summary
            maxlength: maximum length for summary

        Returns:
            list of summary text
        """

        params = {"texts": texts}
        if minlength:
            params["minlength"] = minlength
        if maxlength:
            params["maxlength"] = maxlength

        return self.execute("post", "batchsummary", params)
