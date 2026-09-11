import chromadb


client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="documents"
)


def add_documents(chunks, embeddings):

    ids = []
    documents = []
    metadatas = []

    for chunk in chunks:

        ids.append(
            f"chunk_{chunk['chunk_id']}_page_{chunk['page']}"
        )

        documents.append(
            chunk["text"]
        )

        metadatas.append({
            "page": chunk["page"]
        })

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )

def clear_collection():
    global collection

    client.delete_collection(
        name="documents"
    )

    collection = client.get_or_create_collection(
        name="documents"
    )