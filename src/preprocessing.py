import pandas as pd
import re


def clean_text(text):

    text = re.sub(r"\s+", " ", str(text))

    text = re.sub(
        r"References.*",
        "",
        text
    )

    return text.strip()


def preprocess_dataset():

    df = pd.read_csv(
        "data/raw/pubmed_articles.csv"
    )

    df["clean_text"] = df["text"].apply(clean_text)

    df = df[
        df["clean_text"].str.len() > 300
    ]

    df.to_csv(
        "data/processed/clean_articles.csv",
        index=False
    )

    print(df.head())


if __name__ == "__main__":
    preprocess_dataset()