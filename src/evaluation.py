from retrieval import retrieve

TEST_QUERIES = [
    "amyloid beta targets",
    "tau protein therapeutics",
    "microglia Alzheimer's targets"
]


def evaluate_retrieval():

    for q in TEST_QUERIES:

        print(f"\nQUERY: {q}")

        results = retrieve(q, k=3)

        for r in results:

            print(
                f"Paper ID: {r['paper_id']}"
            )

            print(
                f"Score: {r['score']}"
            )

            print(r["text"][:300])

            print("-" * 50)


if __name__ == "__main__":
    evaluate_retrieval()