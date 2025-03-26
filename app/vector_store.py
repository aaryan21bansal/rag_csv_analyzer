import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

class VectorStore:
    def __init__(self, dim=384):
        self.index = faiss.IndexFlatL2(dim)
        self.data = {}

    def add_document(self, file_id, texts):
        embeddings = model.encode(texts)
        self.index.add(np.array(embeddings, dtype=np.float32))
        self.data[file_id] = texts

    def search(self, query, top_k=3):
        query_embedding = model.encode([query])
        _, indices = self.index.search(np.array(query_embedding, dtype=np.float32), top_k)
        results = [self.data[file_id][i] for i in indices[0] if i < len(self.data[file_id])]
        return results

vector_store = VectorStore()
