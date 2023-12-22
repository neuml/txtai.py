"""
Example extractor functionality.
 
Implements logic found in this notebook: https://github.com/neuml/txtai/blob/master/examples/05_Extractive_QA_with_txtai.ipynb
"""

from txtai.client import Extractor


def run():
    """
    Main method.
    """

    extractor = Extractor("http://localhost:8000")

    data = [
        "Giants hit 3 HRs to down Dodgers",
        "Giants 5 Dodgers 4 final",
        "Dodgers drop Game 2 against the Giants, 5-4",
        "Blue Jays beat Red Sox final score 2-1",
        "Red Sox lost to the Blue Jays, 2-1",
        "Blue Jays at Red Sox is over. Score: 2-1",
        "Phillies win over the Braves, 5-0",
        "Phillies 5 Braves 0 final",
        "Final: Braves lose to the Phillies in the series opener, 5-0",
        "Lightning goaltender pulled, lose to Flyers 4-1",
        "Flyers 4 Lightning 1 final",
        "Flyers win 4-1"
    ]

    # Run series of questions
    questions = ["What team won the game?", "What was score?"]
    for query in ("Red Sox - Blue Jays", "Phillies - Braves", "Dodgers - Giants", "Flyers - Lightning"):
        print(f"----{query}----")

        queue = [{"name": question, "query": query, "question": question, "snippet": False} for question in questions]
        for result in extractor.extract(queue, data):
            print(f"{result['name']} {result['answer']}")

    # Ad-hoc questions
    question = "What hockey team won?"
    print(f"----{question}----")
    for result in extractor.extract([{"name": question, "query": question, "question": question, "snippet": False}], data):
        print(f"{result['name']} {result['answer']}")

run()
