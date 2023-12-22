"""
API module
"""

import asyncio

from urllib.parse import urlencode

import aiohttp


class API:
    """
    Base API class.
    """

    def __init__(self, url):
        """
        Creates a new API instance.

        Args:
            config: cluster configuration
        """

        # Server URL
        self.url = url

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

        async with session.get(url) as resp:
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

        async with session.post(url, json=data) as resp:
            return await resp.json()
