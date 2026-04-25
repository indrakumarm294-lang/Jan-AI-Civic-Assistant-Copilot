import json
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

with open("db/schemes.json") as f:
    data = json.load(f)

texts = [item["name"] + " " + item["description"] for item in data]
embeddings = model.encode(texts)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))

def get_answer(query, category=None):
    query_vec = model.encode([query])

    results = []

    for i, item in enumerate(data):

        if category and item["category"] != category:
            continue

        results.append(item)

    if not results:
        return []

    texts = [r["name"] + " " + r["description"] for r in results]
    embeddings = model.encode(texts)

    temp_index = faiss.IndexFlatL2(embeddings.shape[1])
    temp_index.add(np.array(embeddings))

    distances, indices = temp_index.search(np.array(query_vec), k=3)

    final = []
    for dist, idx in zip(distances[0], indices[0]):
        item = results[idx]
        final.append({
            "name": item["name"],
            "details": item["details"],
            "eligibility": item["eligibility"],
            "score": round(1 / (1 + dist), 2)
        })

    return final