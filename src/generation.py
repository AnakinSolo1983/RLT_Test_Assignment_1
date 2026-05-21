from retrieval import retrieve      # Import the retrieval function.
from transformers import pipeline   # Import the pipeline function.

# Set the generator:
generator = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    device=-1
)

# Generate the answer:
def generate_answer(query):

    docs = retrieve(query, k=3) # Retrieve the documents.

    # Get the context:
    context = "\n\n".join([
        d["text"][:400]
        for d in docs
    ])

    # Set the prompt:
    prompt = f"""
You are a biomedical research assistant.

Question:
{query}

Context:
{context}

Provide:
- therapeutic targets
- therapeutic modalities
- research gaps

Answer:
"""

    response = generator(
        prompt,
        max_new_tokens=120,
        do_sample=False
    )

    answer = response[0]["generated_text"] # Get the answer.

    return answer, docs # Return the answer and the documents.