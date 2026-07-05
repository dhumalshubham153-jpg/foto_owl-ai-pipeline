from pathlib import Path

import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction


class ChromaService:

    def __init__(self):

        self.client = chromadb.PersistentClient(path="./chroma_db")

        self.embedding = SentenceTransformerEmbeddingFunction(
            model_name="all-MiniLM-L6-v2"
        )

        self.style_collection = self.client.get_or_create_collection(
            name="style_guides",
            embedding_function=self.embedding
        )

        self.remotion_collection = self.client.get_or_create_collection(
            name="remotion_docs",
            embedding_function=self.embedding
        )

    def load_documents(self):

        self._load_folder(
            "rag/style_guides",
            self.style_collection
        )

        self._load_folder(
            "rag/remotion_docs",
            self.remotion_collection
        )

    def _load_folder(self, folder_path, collection):

        folder = Path(folder_path)

        for file in folder.glob("*.txt"):

            document = file.read_text(encoding="utf-8")

            collection.upsert(
                ids=[file.stem],
                documents=[document]
            )

    def search_style(self, query):

        result = self.style_collection.query(
            query_texts=[query],
            n_results=1
        )

        return result["documents"][0][0]

    def search_remotion(self, query):

        result = self.remotion_collection.query(
            query_texts=[query],
            n_results=1
        )

        return result["documents"][0][0]