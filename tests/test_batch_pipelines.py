"""Regression tests for batch pipeline requests."""

import unittest
from unittest.mock import patch

from txtai.client import Segmentation, Summary


class BatchPipelineTests(unittest.TestCase):
    def test_batchsegment_request_body(self):
        client = Segmentation()
        with patch.object(client, "execute") as execute:
            for texts in ([], ["one", "two"]):
                with self.subTest(texts=texts):
                    self.assertIs(client.batchsegment(texts), execute.return_value)
                    execute.assert_called_with("post", "batchsegment", texts)

    def test_batchsummary(self):
        client = Summary()
        with patch.object(client, "execute") as execute:
            self.assertIs(client.batchsummary(["one"]), execute.return_value)
            execute.assert_called_once_with("post", "batchsummary", {"texts": ["one"]})

    def test_batchsummary_legacy_name(self):
        client = Summary()
        with patch.object(client, "execute") as execute:
            self.assertIs(client.batchsimilarity(["one"], 2, 8), execute.return_value)
            execute.assert_called_once_with("post", "batchsummary", {"texts": ["one"], "minlength": 2, "maxlength": 8})
