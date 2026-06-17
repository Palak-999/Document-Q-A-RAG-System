import streamlit as st

from langchain_ollama import ChatOllama
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

# Embedding model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load vector database
db = FAISS.load_local(
    "vectorstore",
    embedding_model,
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever(search_kwargs={"k": 3})

# Local LLM
llm = ChatOllama(
    model="llama3.2"
)

st.title("📚 Notes RAG Chatbot")

question = st.text_input("Ask a question")

if question:

    docs = retriever.invoke(question)

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
    Answer ONLY from the context.

    Context:
    {context}

    Question:
    {question}
    """

    response = llm.invoke(prompt)

    st.write(response.content)