import faiss
import numpy as np

class VectorStore:
    def __init__(self):
        self.index = faiss.IndexFlatL2(1536)
        self.entries = []

    # Add a new entry to the vector store
    def add(self, entry_text: str, embedding: list[float]):
        self.index.add(np.array([embedding])).astype('float32')
        self.entries.append((entry_text))

    # Query the vector store for the most similar entries
    def query(self, query_embedding: list[float], k: int = 5):
        distances, indices = self.index.search(np.array([query_embedding]), k)
        return [self.entries[i][0] for i in indices[0]]

store = VectorStore()

