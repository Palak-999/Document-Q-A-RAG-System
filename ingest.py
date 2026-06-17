from utils.loader import load_pdf
from utils.splitter import split_docs
from utils.embeddings import get_embedding_model

from langchain_community.vectorstores import FAISS

print("Loading PDF...")

docs = load_pdf("data/Notes.pdf")

print(f"Loaded {len(docs)} pages")

print("Splitting document...")

chunks = split_docs(docs)

print(f"Created {len(chunks)} chunks")

print("Loading embedding model...")

embedding_model = get_embedding_model()

print("Creating FAISS vector database...")

vector_db = FAISS.from_documents(
    chunks,
    embedding_model
)

vector_db.save_local("vectorstore")

print("✅ Vector database saved successfully!")