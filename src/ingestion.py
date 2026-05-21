from Bio import Entrez  # Import Entrez.
import pandas as pd     # Import pandas.
from tqdm import tqdm   # Import tqdm.

Entrez.email = "your_email@example.com" # Set the email.

# Set the search terms:
SEARCH_TERMS = [
    "Alzheimer therapeutic targets",
    "Alzheimer disease drug targets",
    "Alzheimer targets"
]

# Search PubMed:
def search_pubmed(query, retmax=20):
    
    # Search PubMed:
    handle = Entrez.esearch(
        db="pubmed",
        term=query,
        retmax=retmax
    )

    record = Entrez.read(handle) # Read the handle.

    return record["IdList"] # Return the list of IDs.


# Fetch the article:
def fetch_article(pmid):
    
    # Fetch the article:
    handle = Entrez.efetch(
        db="pubmed",
        id=pmid,
        rettype="abstract",
        retmode="text"
    )

    text = handle.read() # Read the handle.

    # Return the article:
    return {
        "paper_id": pmid,
        "text": text
    }

# Build the dataset:
def build_dataset():
    
    all_articles = [] # Initialize the list of articles.

    # Iterate through the search terms:
    for term in SEARCH_TERMS: 
        
        ids = search_pubmed(term) # Search PubMed.

        # Iterate through the IDs:
        for pmid in tqdm(ids): 

            try:

                article = fetch_article(pmid) # Fetch the article.
                article["query"] = term # Add the query.

                all_articles.append(article) # Add the article to the list.

            except Exception as e:

                print(f"Error for {pmid}: {e}")

    df = pd.DataFrame(all_articles) # Convert the list of articles to a DataFrame.

    df.drop_duplicates(subset=["paper_id"], inplace=True) # Drop duplicates.

    # Save the DataFrame:
    df.to_csv(
        "data/raw/pubmed_articles.csv",
        index=False
    )

    print(df.head()) # Print the head of the DataFrame.
    print(f"Total articles: {len(df)}") # Print the total number of articles.


if __name__ == "__main__":
    
    build_dataset() # Build the dataset.