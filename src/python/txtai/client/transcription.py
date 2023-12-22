"""
Transcription module
"""

from .api import API


class Transcription(API):
    """
    Transcription instance.
    """

    def transcribe(self, file):
        """
        Transcribes audio files to text.

        Args:
            file: file to transcribe

        Returns:
            transcribed text
        """

        return self.execute("get", "transcribe", {"file": file})

    def batchtranscribe(self, files):
        """
        Transcribes audio files to text.

        Args:
            files: list of files to transcribe

        Returns:
            list of transcribed text
        """

        return self.execute("post", "batchtranscribe", files)
