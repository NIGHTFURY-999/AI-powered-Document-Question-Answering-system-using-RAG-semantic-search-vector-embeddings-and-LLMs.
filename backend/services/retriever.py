from services.vector_store import collection
from services.embedding_service import create_embedding


def search_documents(query: str, top_k: int = 3):

    query_embedding = create_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k
    )

    return results