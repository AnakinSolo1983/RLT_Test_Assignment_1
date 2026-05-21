# Alzheimer RAG Agent

RAG-based biomedical assistant for discovering and analyzing potential therapeutic targets for Alzheimer's disease.

## Overview

This project implements a Retrieval-Augmented Generation (RAG) system for biomedical literature analysis focused on Alzheimer's disease therapeutic targets.

The system:

- collects scientific articles from PubMed;
- preprocesses biomedical text;
- builds vector embeddings;
- performs semantic retrieval using FAISS;
- generates grounded answers using a local language model;
- provides an interactive Streamlit interface for researchers.

The goal is to help researchers quickly identify:

- promising therapeutic targets;
- therapeutic modalities;
- emerging research directions;
- gaps in current evidence.

---

# Features

## Data Collection

- PubMed ingestion using Biopython Entrez API
- Automatic article retrieval
- Biomedical abstract extraction

## Preprocessing

- Text cleaning
- Deduplication
- Filtering low-quality documents

## Retrieval

- Sentence-transformer embeddings
- FAISS vector similarity search
- Semantic retrieval of biomedical literature

## Generation

- Local HuggingFace language model
- Retrieval-Augmented Generation (RAG)
- Source-grounded answers

## Interface

- Streamlit web application
- Interactive biomedical querying
- Retrieved source visualization

---

# Architecture

```text
User Query
    ↓
Embedding Model
    ↓
FAISS Retrieval
    ↓
Top-k Relevant Papers
    ↓
LLM Generation
    ↓
Grounded Biomedical Answer
```

---

# Project Structure

```text
alzheimer-rag-agent/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── ingestion.py
│   ├── preprocessing.py
│   ├── embeddings.py
│   ├── retrieval.py
│   ├── generation.py
│   ├── evaluation.py
│   └── utils.py
│
└── app/
    └── streamlit_app.py
```

---

# Installation

## 1. Clone Repository

```bash
git clone <your_repository_url>
cd alzheimer-rag-agent
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Pipeline

## Step 1 — Collect PubMed Articles

```bash
python src/ingestion.py
```

This downloads biomedical articles related to:

- Alzheimer therapeutic targets
- Alzheimer drug targets
- Alzheimer disease targets

Output:

```text
data/raw/pubmed_articles.csv
```

---

## Step 2 — Preprocess Text

```bash
python src/preprocessing.py
```

Performs:

- text cleaning;
- whitespace normalization;
- low-quality document filtering.

Output:

```text
data/processed/clean_articles.csv
```

---

## Step 3 — Build Embeddings + FAISS Index

```bash
python src/embeddings.py
```

Creates:

- sentence embeddings;
- FAISS vector index;
- serialized document store.

Outputs:

```text
data/processed/faiss_index.bin
data/processed/documents.pkl
```

---

## Step 4 — Run Streamlit Application

```bash
streamlit run app/streamlit_app.py
```

The application will open at:

```text
http://localhost:8501
```

---

# Example Questions

## General Questions

```text
What are potential therapeutic targets for Alzheimer's disease?
```

```text
What are promising therapeutic targets beyond amyloid-beta?
```

---

## Mechanistic Questions

```text
How does neuroinflammation contribute to Alzheimer's disease?
```

```text
What role do microglia play in Alzheimer's disease progression?
```

---

## Therapeutic Modalities

```text
Which Alzheimer's targets are suitable for monoclonal antibodies?
```

```text
Which targets are druggable with small molecules?
```

---

## Research Gap Questions

```text
What additional studies are needed to validate Alzheimer's therapeutic targets?
```

```text
What challenges exist in translating Alzheimer's targets into therapies?
```

---

# Models Used

## Embedding Model

### `BAAI/bge-base-en-v1.5`

Chosen because:

- strong semantic retrieval performance;
- lightweight and efficient;
- good biomedical retrieval quality.

---

## Generation Model

### `TinyLlama/TinyLlama-1.1B-Chat-v1.0`

Chosen because:

- lightweight local inference;
- no paid API required;
- reproducible pipeline;
- suitable for CPU inference.

---

# Evaluation

The retrieval system was evaluated qualitatively using biomedical queries.

Evaluation criteria included:

- relevance of retrieved papers;
- semantic consistency;
- grounding quality of generated answers;
- biomedical plausibility.

---

# Future Improvements

## Multi-Modal Extensions

The system can be extended to additional modalities:

### Genomics

- gene expression profiles;
- GWAS datasets;
- transcriptomics.

### Proteomics

- protein interaction networks;
- biomarker analysis.

### Medical Imaging

- MRI;
- PET scans;
- histopathology.

### Clinical Data

- EHRs;
- clinical trials;
- patient cohorts.

---

# Potential Technical Improvements

- hybrid retrieval (BM25 + dense retrieval);
- reranking models;
- larger biomedical LLMs;
- citation-aware generation;
- agentic workflows;
- LangChain integration;
- vector databases (Qdrant, Weaviate, Chroma).

---

# Technologies Used

- Python
- Streamlit
- FAISS
- HuggingFace Transformers
- Sentence Transformers
- PubMed / Biopython
- Pandas
- PyTorch

---

# Example Output

```text
Potential therapeutic targets for Alzheimer's disease include:

- amyloid-beta;
- tau protein;
- microglial pathways;
- O-GlcNAcase;
- gut-brain axis signaling.

Potential therapeutic modalities include monoclonal antibodies,
small molecules, antisense oligonucleotides, and microbiome-targeted interventions.

Research gaps include limited long-term clinical evidence,
safety concerns, and insufficient validation in large-scale studies.
```

---

# Part 4 — Additional Questions

## 1. What additional data modalities can this solution be extended to?

The current system works with biomedical text data from scientific articles. However, the architecture can be extended to several additional modalities relevant to Alzheimer's disease research.

### Genomics

Possible data sources:

- GWAS datasets;
- gene expression profiles;
- transcriptomics data;
- single-cell RNA sequencing.

Potential applications:

- identifying gene-level therapeutic targets;
- discovering disease-associated mutations;
- pathway enrichment analysis.

---

### Proteomics

Possible data sources:

- protein interaction networks;
- mass spectrometry datasets;
- biomarker databases.

Potential applications:

- identifying dysregulated proteins;
- analyzing protein-protein interactions;
- discovering druggable pathways.

---

### Medical Imaging

Possible modalities:

- MRI;
- PET scans;
- histopathology images.

Potential applications:

- detecting neurodegeneration patterns;
- correlating imaging biomarkers with molecular targets;
- multimodal disease progression modeling.

---

### Clinical Data

Possible data sources:

- electronic health records (EHR);
- clinical trial data;
- patient cohorts.

Potential applications:

- patient stratification;
- treatment response prediction;
- real-world evidence analysis.

---

### Knowledge Graphs

Possible data sources:

- biomedical ontologies;
- drug-target databases;
- pathway databases.

Potential applications:

- relation extraction;
- target prioritization;
- explainable reasoning over biomedical entities.

---

# 2. How can the system be extended to support these modalities?

Several approaches can be used to integrate multimodal biomedical data into the RAG system.

## Multimodal Embeddings

Different encoders can be used for different data types:

- text encoders for scientific literature;
- CNN/ViT models for medical imaging;
- graph neural networks for molecular graphs;
- tabular encoders for clinical data.

The embeddings can then be stored in a shared vector database for unified retrieval.

---

## Hybrid Retrieval

The retrieval pipeline can be extended with:

- dense retrieval;
- sparse retrieval (BM25);
- graph-based retrieval;
- metadata filtering.

This would improve retrieval quality and domain specificity.

---

## Agentic Workflows

The system can be expanded into a multi-agent architecture:

- literature retrieval agent;
- pathway analysis agent;
- target validation agent;
- clinical evidence agent.

This would allow more complex biomedical reasoning workflows.

---

## Reranking Models

Cross-encoder rerankers can improve retrieval precision by reranking retrieved documents before generation.

Potential models:

- BAAI/bge-reranker;
- BioBERT rerankers;
- MiniLM cross-encoders.

---

## Biomedical Fine-Tuning

The generation model can be fine-tuned on:

- PubMedQA;
- BioASQ;
- biomedical summarization datasets.

This would improve biomedical reasoning and answer quality.

---

# 3. Which models were selected and why?

## Embedding Model

### `BAAI/bge-base-en-v1.5`

Reasons for selection:

- strong semantic retrieval quality;
- lightweight and efficient;
- good performance on scientific text;
- suitable for dense vector retrieval with FAISS.

This model is used to generate embeddings for biomedical articles.

---

## Vector Database

### FAISS

Reasons for selection:

- efficient similarity search;
- scalable vector indexing;
- lightweight local deployment;
- widely used in RAG systems.

FAISS is used for semantic retrieval of biomedical papers.

---

## Generation Model

### `TinyLlama/TinyLlama-1.1B-Chat-v1.0`

Reasons for selection:

- lightweight local inference;
- no paid API required;
- suitable for CPU execution;
- reproducible deployment.

The model generates grounded answers based on retrieved biomedical context.

---

## Alternative Models Considered

### FLAN-T5

Advantages:

- strong instruction-following capabilities;
- good summarization quality.

Limitations:

- higher memory usage;
- GPU memory limitations on local hardware.

---

### OpenAI GPT Models

Advantages:

- stronger reasoning quality;
- better biomedical summarization.

Limitations:

- API costs;
- quota limitations;
- dependence on external services.

For reproducibility and local execution, an open-source local model was preferred.

---

# Final Conclusion

The implemented system demonstrates a complete Retrieval-Augmented Generation pipeline for biomedical research assistance.

The architecture supports future expansion toward:

- multimodal biomedical analysis;
- clinical decision support;
- target discovery workflows;
- agentic biomedical reasoning systems.

The solution combines semantic retrieval, local language models, and scientific literature grounding to support Alzheimer's disease therapeutic target exploration.
