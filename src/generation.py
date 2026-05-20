from retrieval import retrieve

from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    device=-1
)


def generate_answer(query):

    docs = retrieve(query, k=3)

    context = "\n\n".join([
        d["text"][:400]
        for d in docs
    ])

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

    answer = response[0]["generated_text"]

    return answer, docs