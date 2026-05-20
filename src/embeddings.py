import pandas as pd
import faiss
import numpy as np
import pickle

from sentence_transformers import SentenceTransformer

MODEL_NAME = "BAAI/bge-base-en-v1.5"

model = SentenceTransformer(MODEL_NAME)


def build_embeddings():

    df = pd.read_csv(
        "data/processed/clean_articles.csv"
    )

    texts = df["clean_text"].tolist()

    embeddings = model.encode(
        texts,
        show_progress_bar=True
    )

    embeddings = np.array(
        embeddings
    ).astype("float32")

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(embeddings)

    faiss.write_index(
        index,
        "data/processed/faiss_index.bin"
    )

    with open(
        "data/processed/documents.pkl",
        "wb"
    ) as f:

        pickle.dump(
            df.to_dict("records"),
            f
        )

    print("Embeddings saved successfully")


if __name__ == "__main__":
    build_embeddings()