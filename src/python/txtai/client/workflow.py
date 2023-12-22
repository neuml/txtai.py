"""
Workflow module
"""

from .api import API


class Workflow(API):
    """
    Workflow instance.
    """

    def workflow(self, name, elements):
        """
        Executes a named workflow using elements as input.

        Args:
            name: workflow name
            elements: list of elements to run through workflow

        Returns:
            list of processed elements
        """

        return self.execute("post", "workflow", {"name": name, "elements": elements})
