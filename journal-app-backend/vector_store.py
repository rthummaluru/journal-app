import faiss
import numpy as np
from typing import List

class VectorStore:

    #setup faiss index + storage
    def __init__(self):
        self.index = faiss.IndexFlatL2(1536)
        self.entries = []
    
    #add a vector + orginial text
    def add(self, entry_text: str, embedding: List[float]):
        vector = np.array([embedding]).astype('float32')
        self.index.add(vector)
        self.entries.append(entry_text)

    #search for top k similar vectors
    def search(self, query_embedding: List[float], k: int = 5):
        query_vector = np.array([query_embedding]).astype('float32')
        distances, indices = self.index.search(query_vector, k)
        return [self.entries[i] for i in indices[0]]

# Create a singleton instance
store = VectorStore()
        