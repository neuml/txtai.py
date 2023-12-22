""" 
Example embeddings functionality.
 
Implements functionality found in this notebook: https://github.com/neuml/txtai/blob/master/examples/01_Introducing_txtai.ipynb
"""

from txtai.client import Embeddings


def run():
    """
    Main method.
    """

    embeddings = Embeddings("http://localhost:8000")

    data = [
        "US tops 5 million confirmed virus cases",
        "Canada's last fully intact ice shelf has suddenly collapsed, forming a Manhattan-sized iceberg",
        "Beijing mobilises invasion craft along coast as Taiwan tensions escalate",
        "The National Park Service warns against sacrificing slower friends in a bear attack",
        "Maine man wins $1M from $25 lottery ticket",
        "Make huge profits without work, earn up to $100,000 a day",
    ]

    print("Running similarity queries")
    print(f"{'Query':<20} Best Match")
    print("-" * 50)

    # Calculate similarity
    for query in ("feel good story", "climate change", "public health story", "war", "wildlife", "asia", "lucky", "dishonest junk"):
        results = embeddings.similarity(query, data)
        uid = results[0]["id"]

        # Print text
        print(f"{query:<20} {data[uid]}")

    # Index dataset
    embeddings.add([{"id": i, "text": x} for i, x in enumerate(data)])
    embeddings.index()

    print()
    print("Building an Embeddings index")
    print(f"{'Query':<20} Best Match")
    print("-" * 50)

    # Run an embeddings search for each query
    for query in ("feel good story", "climate change", "public health story", "war", "wildlife", "asia", "lucky", "dishonest junk"):
        results = embeddings.search(query, 1)
        uid = results[0]["id"]

        # Print text
        print(f"{query:<20} {data[uid]}")

    # Update data
    data[0] = "See it: baby panda born"

    embeddings.delete([5])
    embeddings.add([{"id": 0, "text": data[0]}])
    embeddings.upsert()

    print()
    print("Test delete/upsert/count")
    print(f"{'Query':<20} Best Match")
    print("-" * 50)

    query = "feel good story"
    results = embeddings.search(query, 1)
    uid = results[0]["id"]
    print(f"{query:<20} {data[uid]}")

    # Show total count
    count = embeddings.count()
    print()
    print(f"Total Count: {count}")


run()
