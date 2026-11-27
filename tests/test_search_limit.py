"""Request parameters for single and batch search."""

import unittest
from unittest.mock import patch

from txtai.client import Embeddings


class SearchLimitTests(unittest.TestCase):
    def test_explicit_zero_and_default(self):
        client = Embeddings()
        with patch.object(client, "execute") as execute:
            client.search("apple", limit=0)
            execute.assert_called_with("get", "search", {"query": "apple", "limit": 0})
            client.search("apple")
            execute.assert_called_with("get", "search", {"query": "apple"})
            client.batchsearch(["apple"], limit=0)
            execute.assert_called_with("post", "batchsearch", {"queries": ["apple"], "limit": 0})
            client.batchsearch(["apple"])
            execute.assert_called_with("post", "batchsearch", {"queries": ["apple"]})
