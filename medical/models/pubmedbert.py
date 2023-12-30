"""
Model Card for Meditron-7B-v1.0
7 billion parameters model adapted to the medical domain from Llama-2-7B
"""
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import (DirectoryLoader, PyPDFLoader)
from langchain.vectorstores import Qdrant
from langchain.embeddings import SentenceTransformerEmbeddings

embeddings = SentenceTransformerEmbeddings(model_name = "NeuML/pubmedbert-base-embeddings")

print(embeddings)

loader = DirectoryLoader('../Data/',glob="**/*.pdf", show_progress=True, loader_cls=PyPDFLoader)

document = loader.load()

text_splitter = RecursiveCharacterTextSplitter()

texts = text_splitter.split_documents(documents=document)

url = "http://localhost:6333/dashboard"

qdrant = Qdrant.from_documents(
    texts, embeddings, url = url, prefer_grpc= False, collection_name = "vector_database"
)
