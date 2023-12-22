"""
Example pipeline and workflow functionality.

Uses files from txtai unit tests: https://github.com/neuml/txtai/releases/download/v2.0.0/tests.tar.gz
"""

from txtai.client import Segmentation, Textractor, Summary, Transcription, Translation, Workflow


def run():
    """
    Main method.
    """

    service = "http://localhost:8000"

    segment = Segmentation(service)

    sentences = "This is a test. And another test."

    print("---- Segmented Text ----")
    print(segment.segment(sentences))

    textractor = Textractor(service)
    text = textractor.textract("/tmp/txtai/article.pdf")

    print("\n---- Extracted Text ----")
    print(text)

    summary = Summary(service)
    summarytext = summary.summary(text)

    print("\n---- Summary Text ----")
    print(summarytext)

    translate = Translation(service)
    translation = translate.translate(summarytext, "es")

    print("\n---- Summary Text in Spanish ----")
    print(translation)

    workflow = Workflow(service)
    output = workflow.workflow("sumspanish", ["file:///tmp/txtai/article.pdf"])

    print("\n---- Workflow [Extract Text->Summarize->Translate] ----")
    print(output)

    transcribe = Transcription(service)
    transcription = transcribe.transcribe("/tmp/txtai/Make_huge_profits.wav")

    print("\n---- Transcribed Text ----")
    print(transcription)


run()
