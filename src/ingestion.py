from Bio import Entrez
import pandas as pd
from tqdm import tqdm

Entrez.email = "your_email@example.com"

SEARCH_TERMS = [
    "Alzheimer therapeutic targets",
    "Alzheimer disease drug targets",
    "Alzheimer targets"
]


def search_pubmed(query, retmax=20):
    handle = Entrez.esearch(
        db="pubmed",
        term=query,
        retmax=retmax
    )

    record = Entrez.read(handle)

    return record["IdList"]


def fetch_article(pmid):
    handle = Entrez.efetch(
        db="pubmed",
        id=pmid,
        rettype="abstract",
        retmode="text"
    )

    text = handle.read()

    return {
        "paper_id": pmid,
        "text": text
    }


def build_dataset():
    all_articles = []

    for term in SEARCH_TERMS:
        ids = search_pubmed(term)

        for pmid in tqdm(ids):

            try:
                article = fetch_article(pmid)
                article["query"] = term

                all_articles.append(article)

            except Exception as e:
                print(f"Error for {pmid}: {e}")

    df = pd.DataFrame(all_articles)

    df.drop_duplicates(subset=["paper_id"], inplace=True)

    df.to_csv(
        "data/raw/pubmed_articles.csv",
        index=False
    )

    print(df.head())
    print(f"Total articles: {len(df)}")


if __name__ == "__main__":
    build_dataset()