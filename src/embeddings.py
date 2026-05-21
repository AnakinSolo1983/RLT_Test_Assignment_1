import pandas as pd # Import pandas
import faiss        # Import faiss
import numpy as np  # Import numpy
import pickle       # Import pickle

from sentence_transformers import SentenceTransformer # Import SentenceTransformer

MODEL_NAME = "BAAI/bge-base-en-v1.5" # Set the model name.

model = SentenceTransformer(MODEL_NAME) # Load the model.

# Build the embeddings:
def build_embeddings():

    # Read the clean articles:
    df = pd.read_csv(
        "data/processed/clean_articles.csv"
    )

    texts = df["clean_text"].tolist() # Get the clean text.

    # Encode the clean text:
    embeddings = model.encode(
        texts,
        show_progress_bar=True
    )

    # Convert the embeddings to a numpy array:
    embeddings = np.array(
        embeddings
    ).astype("float32")

    # Get the dimension of the embeddings:
    dimension = embeddings.shape[1]

    index = faiss.IndexFlatL2(dimension) # Create a FAISS index.

    index.add(embeddings) # Add the embeddings to the index.

    # Save the FAISS index:
    faiss.write_index(
        index,
        "data/processed/faiss_index.bin"
    )

    # Save the documents:
    with open(
        "data/processed/documents.pkl",
        "wb"
    ) as f:

        pickle.dump(
            df.to_dict("records"),
            f
        )

    print("Embeddings saved successfully") # Print that the embeddings were saved successfully.


if __name__ == "__main__":

    build_embeddings() # Build the embeddings.