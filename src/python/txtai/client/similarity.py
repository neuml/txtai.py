"""
Similarity module
"""

from .api import API


class Similarity(API):
    """
    Similarity instance.
    """

    def similarity(self, query, texts):
        """
        Computes the similarity between query and list of text. Returns a list of
        {id: value, score: value} sorted by highest score, where id is the index
        in texts.

        Args:
            query: query text
            texts: list of text

        Returns:
            list of {id: value, score: value}
        """

        return self.execute("post", "similarity", {"query": query, "texts": texts})

    def batchsimilarity(self, queries, texts):
        """
        Computes the similarity between list of queries and list of text. Returns a list
        of {id: value, score: value} sorted by highest score per query, where id is the
        index in texts.

        Args:
            queries: queries text
            texts: list of text

        Returns:
            list of {id: value, score: value} per query
        """

        return self.execute("post", "batchsimilarity", {"queries": queries, "texts": texts})
