"""
API module
"""

from .api import API


class Embeddings(API):
    """
    Embeddings instance.
    """

    def search(self, query, limit=None, weights=None, index=None):
        """
        Finds documents most similar to the input query. This method will run either an index search
        or an index + database search depending on if a database is available.

        Args:
            query: input query
            limit: maximum results
            weights: hybrid score weights, if applicable
            index: index name, if applicable

        Returns:
            list of {id: value, score: value} for index search, list of dict for an index + database search
        """

        # Build URL
        action = "search"
        data = {"query": query}
        if limit:
            data["limit"] = limit
        if weights:
            data["weights"] = weights
        if index:
            data["index"] = index

        # Run query
        return self.execute("get", action, data)

    def batchsearch(self, queries, limit=None, weights=None, index=None):
        """
        Finds documents most similar to the input queries. This method will run either an index search
        or an index + database search depending on if a database is available.

        Args:
            queries: input queries
            limit: maximum results
            weights: hybrid score weights, if applicable
            index: index name, if applicable

        Returns:
            list of {id: value, score: value} per query for index search, list of dict per query for an index + database search
        """

        # POST parameters
        params = {"queries": queries}
        if limit:
            params["limit"] = limit
        if weights:
            params["weights"] = weights
        if index:
            params["index"] = index

        # Run query
        return self.execute("post", "batchsearch", params)

    def add(self, documents):
        """
        Adds a batch of documents for indexing.

        Args:
            documents: list of {id: value, text: value}
        """

        self.execute("post", "add", documents)

    def index(self):
        """
        Builds an embeddings index for previously batched documents.
        """

        self.execute("get", "index")

    def upsert(self):
        """
        Runs an embeddings upsert operation for previously batched documents.
        """

        self.execute("get", "upsert")

    def delete(self, ids):
        """
        Deletes from an embeddings index. Returns list of ids deleted.

        Args:
            ids: list of ids to delete

        Returns:
            ids deleted
        """

        return self.execute("post", "delete", ids)

    def reindex(self, config, function=None):
        """
        Recreates this embeddings index using config. This method only works if document content storage is enabled.

        Args:
            config: new config
            function: optional function to prepare content for indexing
        """

        self.execute("post", "reindex", {"config": config, "function": function})

    def count(self):
        """
        Total number of elements in this embeddings index.

        Returns:
            number of elements in embeddings index
        """

        return self.execute("get", "count")

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

    def transform(self, text):
        """
        Transforms text into an embeddings array.

        Args:
            text: input text

        Returns:
            embeddings array
        """

        return self.execute("get", "transform", {"text": text})

    def batchtransform(self, texts):
        """
        Transforms list of text into embeddings arrays.

        Args:
            texts: list of text

        Returns:
            embeddings arrays
        """

        return self.execute("post", "batchtransform", texts)
