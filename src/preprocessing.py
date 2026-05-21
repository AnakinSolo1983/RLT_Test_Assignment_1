import pandas as pd # Import pandas.
import re           # Import re.

# Clean the text:
def clean_text(text):

    text = re.sub(r"\s+", " ", str(text)) # Remove extra whitespace.

    # Remove references:
    text = re.sub(
        r"References.*",
        "",
        text
    )

    return text.strip() # Remove leading/trailing whitespace.


# Preprocess the dataset:
def preprocess_dataset():

    # Read the dataset:
    df = pd.read_csv(
        "data/raw/pubmed_articles.csv"
    )

    df["clean_text"] = df["text"].apply(clean_text) # Clean the text.

    # Filter out short texts:
    df = df[
        df["clean_text"].str.len() > 300
    ]

    # Save the cleaned dataset:
    df.to_csv(
        "data/processed/clean_articles.csv",
        index=False
    )

    print(df.head()) # Print the head of the DataFrame.


if __name__ == "__main__":

    preprocess_dataset() # Preprocess the dataset.