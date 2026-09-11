from services.document_processor import extract_text_from_pdf
from services.chunker import chunk_text
from services.embedding_service import create_embeddings


pages = extract_text_from_pdf("sample.pdf")


all_chunks = []

for page in pages:
    chunks = chunk_text(
        page["text"],
        page["page"]
    )

    all_chunks.extend(chunks)


embeddings = create_embeddings(all_chunks)


print("Number of chunks:", len(all_chunks))
print("Number of embeddings:", len(embeddings))
print("Embedding dimensions:", len(embeddings[0]))