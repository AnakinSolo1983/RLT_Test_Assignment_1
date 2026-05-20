import faiss
import pickle
import numpy as np

from sentence_transformers import SentenceTransformer

MODEL_NAME = "BAAI/bge-base-en-v1.5"

model = SentenceTransformer(MODEL_NAME)

index = faiss.read_index(
    "data/processed/faiss_index.bin"
)

with open(
    "data/processed/documents.pkl",
    "rb"
) as f:

    documents = pickle.load(f)


def retrieve(query, k=5):

    query_embedding = model.encode([query])

    query_embedding = np.array(
        query_embedding
    ).astype("float32")

    distances, indices = index.search(
        query_embedding,
        k
    )

    results = []

    for idx, dist in zip(indices[0], distances[0]):

        doc = documents[idx]

        results.append({
            "paper_id": doc["paper_id"],
            "text": doc["clean_text"],
            "score": float(dist)
        })

    return results


if __name__ == "__main__":

    query = (
        "What are therapeutic targets "
        "for Alzheimer's disease?"
    )

    results = retrieve(query)

    for r in results:

        print(r["paper_id"])
        print(r["score"])
        print(r["text"][:500])

        print("-" * 80)