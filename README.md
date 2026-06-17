# 📚 Document Q&A RAG System

A Retrieval-Augmented Generation (RAG) chatbot that allows users to ask questions from their PDF documents and receive context-aware answers using semantic search and a local Large Language Model (LLM).

---

## 🚀 Project Overview

Large Language Models (LLMs) do not have access to your private documents by default. This project solves that problem using Retrieval-Augmented Generation (RAG).

The system:

* Loads PDF documents
* Splits documents into smaller chunks
* Converts text chunks into vector embeddings
* Stores embeddings in a FAISS vector database
* Retrieves relevant chunks based on user questions
* Uses a local LLM (Llama 3.2 via Ollama) to generate answers

This enables users to chat with their own documents without relying on external APIs.

---

## 🏗️ Architecture

```text
                    ┌───────────────────┐
                    │     PDF File      │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │   PDF Loader      │
                    │ (PyPDFLoader)     │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Text Chunking     │
                    │ RecursiveSplitter │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Embeddings Model  │
                    │ all-MiniLM-L6-v2  │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │  FAISS Vector DB  │
                    └─────────┬─────────┘
                              │
               User Question  │
                              ▼
                    ┌───────────────────┐
                    │    Retriever      │
                    └─────────┬─────────┘
                              │
                    Relevant Chunks
                              │
                              ▼
                    ┌───────────────────┐
                    │  Ollama LLM       │
                    │   Llama 3.2       │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Generated Answer  │
                    └───────────────────┘
```

---

## 🛠️ Tech Stack

| Component            | Technology            |
| -------------------- | --------------------- |
| Programming Language | Python                |
| Framework            | LangChain             |
| UI                   | Streamlit             |
| Vector Database      | FAISS                 |
| Embeddings           | Sentence Transformers |
| Embedding Model      | all-MiniLM-L6-v2      |
| LLM Runtime          | Ollama                |
| Language Model       | Llama 3.2             |
| PDF Processing       | PyPDF                 |

---

## 📂 Project Structure

```text
document-rag-chatbot/
│
├── app.py
├── ingest.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   └── Notes.pdf
│
├── utils/
│   ├── __init__.py
│   ├── loader.py
│   ├── splitter.py
│   └── embeddings.py
│
└── vectorstore/
    ├── index.faiss
    └── index.pkl
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/Palak-999/Document-Q-A-RAG-System.git
cd Document-Q-A-RAG-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🤖 Install Ollama

Download Ollama:

https://ollama.com/download

Pull Llama 3.2:

```bash
ollama pull llama3.2
```

Verify installation:

```bash
ollama run llama3.2
```

---

## 📥 Build Vector Database

Place your PDF inside the `data` folder and run:

```bash
python ingest.py
```

This will:

* Load PDF
* Split text into chunks
* Generate embeddings
* Store vectors in FAISS

---

## ▶️ Run Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

## 💡 Example Questions

```text
What is Machine Learning?

Explain Transfer Learning.

What are the advantages of Transformers?

Summarize Chapter 2.
```

---

## 📖 Key Concepts Learned

### Retrieval-Augmented Generation (RAG)

Combines information retrieval with LLM-based generation.

### Chunking

Splitting large documents into smaller manageable sections.

### Embeddings

Numerical vector representation of text used for semantic search.

### Semantic Search

Search based on meaning rather than exact keyword matching.

### Vector Database

Stores embeddings and enables similarity search.

### FAISS

Facebook AI Similarity Search used for fast vector retrieval.

### Local LLM

Runs language models directly on the user's machine using Ollama.

---

## 🎯 Learning Outcomes

Through this project I learned:

* LangChain Fundamentals
* PDF Processing
* Text Chunking Strategies
* Embeddings and Vector Representations
* Semantic Search
* FAISS Vector Databases
* Retrieval-Augmented Generation (RAG)
* Local LLM Integration with Ollama
* Streamlit Application Development
* Git and GitHub Workflow

---

## 🔮 Future Improvements

* Multi-PDF Support
* Chat History Memory
* Source Citations
* Hybrid Search
* Re-ranking
* Conversational RAG
* Docker Deployment
* Cloud Hosting

---

## 👩‍💻 Author

**Palak**

Aspiring AI Engineer passionate about Generative AI, RAG Systems, Agentic AI, and LLM Applications.
