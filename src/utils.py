import pandas as pd
import matplotlib.pyplot as plt


def document_length_histogram(csv_path):

    df = pd.read_csv(csv_path)

    lengths = df["clean_text"].apply(len)

    plt.figure(figsize=(10, 6))

    plt.hist(lengths, bins=20)

    plt.xlabel("Document Length")
    plt.ylabel("Count")

    plt.title(
        "Distribution of Document Lengths"
    )

    plt.show()