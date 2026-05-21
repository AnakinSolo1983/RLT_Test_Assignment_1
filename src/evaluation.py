from retrieval import retrieve # Import the retrieval function.

# Set the test queries:
TEST_QUERIES = [
    "amyloid beta targets",
    "tau protein therapeutics",
    "microglia Alzheimer's targets"
]

# Evaluate the retrieval:
def evaluate_retrieval():

    # Iterate through the test queries:
    for q in TEST_QUERIES:

        print(f"\nQUERY: {q}") # Print the query.

        results = retrieve(q, k=3) # Retrieve the results.

        # Iterate through the results:
        for r in results:

            # Print the paper ID:
            print(
                f"Paper ID: {r['paper_id']}"
            )

            # Print the score:
            print(
                f"Score: {r['score']}"
            )

            # Print the text:
            print(r["text"][:300])

            # Print the separator:
            print("-" * 50)


if __name__ == "__main__":
    
    evaluate_retrieval() # Evaluate the retrieval.