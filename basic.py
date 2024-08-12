from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma

embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings,
    persist_directory="chroma_langchain_db"
)

import chromadb

persistent