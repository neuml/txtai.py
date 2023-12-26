"""
API module
"""

import asyncio
import os

from urllib.parse import urlencode

import aiohttp


class API:
    """
    Base API class.
    """

    def __init__(self, url=None, token=None):
        """
        Creates a new API instance.

        Args:
            url: API url
            token: API token
        """

        # Server URL
        self.url = url if url else os.environ.get("TXTAI_API_URL")

        # Authorization token
        self.token = token if token else os.environ.get("TXTAI_API_TOKEN")

    def execute(self, method, action, data=None):
        """
        Executes a HTTP action asynchronously.

        Args:
            method: get or post
            action: url action to perform
            data: post parameters

        Returns:
            json results if any
        """

        close = False

        # Use existing loop if available, otherwise create one
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            close = True

        try:
            return loop.run_until_complete(self.run(method, action, data))
        finally:
            # Close loop if it was created in this method
            if close:
                loop.close()

    async def run(self, method, action, data):
        """
        Runs an async action.

        Args:
            method: get or post
            action: url action to perform
            data: post parameters

        Returns:
            json results if any
        """

        async with aiohttp.ClientSession(raise_for_status=True) as session:
            url, task = f"{self.url}/{action}", None
            if method == "post":
                task = asyncio.ensure_future(self.post(session, url, data))
            else:
                task = asyncio.ensure_future(self.get(session, url, data))

            # Run and wait for task to complete
            return await task

    async def get(self, session, url, data):
        """
        Runs an async HTTP GET request.

        Args:
            session: ClientSession
            url: url
            data: url parameters

        Returns:
            json results if any
        """

        # Build URL with parameters
        parameters = urlencode(data) if data else None
        url = f"{url}?{parameters}" if parameters else url

        async with session.get(url, headers=self.headers()) as resp:
            return await resp.json()

    async def post(self, session, url, data):
        """
        Runs an async HTTP POST request.

        Args:
            session: ClientSession
            url: url
            data: data to POST

        Returns:
            json results if any
        """

        async with session.post(url, json=data, headers=self.headers()) as resp:
            return await resp.json()

    def headers(self):
        """
        Default HTTP headers.

        Returns:
            HTTP headers
        """

        return {"Authorization": f"Bearer {self.token}"} if self.token else None
