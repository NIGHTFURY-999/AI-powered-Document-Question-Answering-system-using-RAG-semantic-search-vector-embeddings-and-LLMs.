from services.document_processor import extract_text_from_pdf
from services.chunker import chunk_text
from services.embedding_service import create_embeddings
from services import vector_store


vector_store.clear_collection()


pages = extract_text_from_pdf("sample.pdf")


all_chunks = []

for page in pages:

    chunks = chunk_text(
        page["text"],
        page["page"]
    )

    all_chunks.extend(chunks)


embeddings = create_embeddings(all_chunks)


vector_store.add_documents(
    all_chunks,
    embeddings
)


print("Chunks created:", len(all_chunks))
print("Embeddings created:", len(embeddings))
print("Documents stored:", vector_store.collection.count())