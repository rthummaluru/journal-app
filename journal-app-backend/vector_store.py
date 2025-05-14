import faiss
import numpy as np

class VectorStore:

    #setup faiss index + storage
    def __init__(self):
        self.index = faiss.IndexFlatL2(1536)
        self.entries = []
    
    #add a vector + orginial text
    def add(self, entry_text: str, embedding: list[float]):
        vector = np.array([embedding]).asType("float32")
        self.index.add(vector)
        self.entries.append(entry_text)

    #search for top k similar vectors
    def search(self, query_embedding: list[float], k=5):
        query_vector = np.array([query_embedding]).asType("float32")
        distance, index = self.index.search(query_vector, k)
        return [self.entries[i] for i in index[0]]

        