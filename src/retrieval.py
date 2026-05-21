import faiss        # Import faiss.
import pickle       # Import pickle.
import numpy as np  # Import numpy.

from sentence_transformers import SentenceTransformer # Import SentenceTransformer.

MODEL_NAME = "BAAI/bge-base-en-v1.5" # Set the model name.

model = SentenceTransformer(MODEL_NAME) # Load the model.

# Load the FAISS index:
index = faiss.read_index(
    "data/processed/faiss_index.bin"
)

# Load the documents:
with open(
    "data/processed/documents.pkl",
    "rb"
) as f:

    documents = pickle.load(f)

# Retrieve the documents:
def retrieve(query, k=5):

    query_embedding = model.encode([query]) # Encode the query.

    # Convert the query embedding to a numpy array:
    query_embedding = np.array(
        query_embedding
    ).astype("float32")

    # Search the FAISS index:
    distances, indices = index.search(
        query_embedding,
        k
    )

    results = [] # Initialize the results list.

    # Iterate through the results:
    for idx, dist in zip(indices[0], distances[0]):

        doc = documents[idx] # Get the document.

        # Append the results:
        results.append({
            "paper_id": doc["paper_id"],
            "text": doc["clean_text"],
            "score": float(dist)
        })

    return results # Return the results.


if __name__ == "__main__":

    # Set the query:
    query = (
        "What are therapeutic targets "
        "for Alzheimer's disease?"
    )

    results = retrieve(query) # Retrieve the documents.

    # Iterate through the results:
    for r in results:

        print(r["paper_id"])    # Print the paper ID.
        print(r["score"])       # Print the score.
        print(r["text"][:500])  # Print the text.

        print("-" * 80)         # Print the separator.