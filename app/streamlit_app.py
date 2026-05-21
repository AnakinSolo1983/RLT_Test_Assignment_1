import streamlit as st # Import Streamlit
import sys             # Import sys

# Add the src directory to sys.path:
sys.path.append("src")

# Import the generate_answer function from the generation module:
from generation import generate_answer

# Set the page configuration:
st.set_page_config(
    page_title="Alzheimer RAG Assistant",
    layout="wide"
)

# Set the title of the app:
st.title(
    "Alzheimer Therapeutic Target Assistant"
)

# Set the markdown of the app:
st.markdown(
    "Ask questions about Alzheimer's therapeutic targets"
)

# Set the text input for the query:
query = st.text_input(
    "Enter your biomedical question"
)

# Set the button for the query:
if st.button("Search"):

    # Set the spinner for the query:
    with st.spinner("Generating answer..."):

        answer, docs = generate_answer(query) # Generate the answer and retrieve the docs.

    # Set the subheader for the answer:
    st.subheader("Generated Answer")

    st.write(answer) # Write the answer.

    st.subheader("Retrieved Sources") # Set the subheader for the retrieved sources.

    # Iterate through the retrieved sources:
    for i, doc in enumerate(docs): 

        # Set the expander for the retrieved sources:
        with st.expander(
            f"Source {i+1} | PMID: {doc['paper_id']}"
        ):

            # Set the similarity score:
            st.write(
                f"Similarity Score: {doc['score']:.4f}"
            )

            st.write(doc["text"][:2000]) # Write the retrieved sources.
