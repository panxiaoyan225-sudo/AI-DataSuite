# run the following command to pull the models:
# ollama pull llama3
# ollama pull nomic-embed-text
# run the following command to install the dependencies:

from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_classic.chains import RetrievalQA
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

doc_dir = os.getenv("my_docu")
if not doc_dir:
    raise SystemExit("Missing my_docu in AI-DataSuite/.env")


def ollama_base_url() -> str:
    """Client URL for Ollama. 0.0.0.0 is a bind address and cannot be dialed."""
    raw = (os.getenv("OLLAMA_HOST") or "127.0.0.1:11434").strip().rstrip("/")
    if raw in {"0.0.0.0", "0.0.0.0:11434", "::", "[::]", "[::]:11434"}:
        return "http://127.0.0.1:11434"
    if "://" not in raw:
        if raw.count(":") == 0:
            raw = f"{raw}:11434"
        raw = f"http://{raw}"
    return raw


def load_docs(folder: str):
    # The reports directory holds HTML and Markdown, not only .txt.
    docs = []
    for pattern in ("*.txt", "*.md", "*.html"):
        loader = DirectoryLoader(
            folder,
            glob=pattern,
            loader_cls=TextLoader,
            loader_kwargs={"encoding": "utf-8"},
            silent_errors=True,
        )
        docs.extend(loader.load())
    if not docs:
        raise SystemExit(f"No .txt, .md, or .html files found in {folder}")
    return docs

def main():
    # Load documents and set up RAG system (run once)
    docs = load_docs(doc_dir)
    print(f"Loaded {len(docs)} documents from {doc_dir}")

    # Chunking for Precision
    # Keeps context together with overlap
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(docs)

    # Local Embeddings & Vector Store
    # Uses Ollama's local embedding model (nomic-embed-text)
    ollama_url = ollama_base_url()
    print(f"Connecting to Ollama at {ollama_url}")
    embeddings = OllamaEmbeddings(model="nomic-embed-text", base_url=ollama_url)
    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./chroma_db",
    )

    # Initialize Local LLM
    llm = ChatOllama(model="deepseek-r1:8b", temperature=0, base_url=ollama_url)

    # Build RAG Chain
    # Connects the retriever to the LLM
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vector_db.as_retriever(search_kwargs={"k": 3}),
    )
    
    # Ask user for query (moved out of main code — no hardcoded query)
    query = input("Please enter your query: ")
    print(f"Processing query: {query}")
    
    # Query the System
    response = qa_chain.invoke({"query": query})
    print(f"Answer: {response['result']}")


if __name__ == "__main__":
    main()