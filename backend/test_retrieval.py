from services.retriever import search_documents


query = "What machine learning projects did I work on?"

results = search_documents(query, top_k=5)


documents = results["documents"][0]
distances = results["distances"][0]
metadatas = results["metadatas"][0]


for i in range(len(documents)):

    print(f"\nRESULT {i + 1}")
    print("-" * 50)

    print("Distance:", distances[i])
    print("Page:", metadatas[i]["page"])
    print("Text:")
    print(documents[i])