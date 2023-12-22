"""
Translation module
"""

from .api import API


class Translation(API):
    """
    Translation instance.
    """

    def translate(self, text, target=None, source=None):
        """
        Translates text from source language into target language.

        Args:
            text: text to translate
            target: target language code, defaults to "en"
            source: source language code, detects language if not provided

        Returns:
            translated text
        """

        params = {"text": text}
        if target:
            params["target"] = target
        if source:
            params["source"] = source

        return self.execute("get", "translate", params)

    def batchtranslate(self, texts, target=None, source=None):
        """
        Translates text from source language into target language.

        Args:
            texts: list of text to translate
            target: target language code, defaults to "en"
            source: source language code, detects language if not provided

        Returns:
            list of translated text
        """

        params = {"texts": texts}
        if target:
            params["target"] = target
        if source:
            params["source"] = source

        return self.execute("post", "batchtranslate", params)
