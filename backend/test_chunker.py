from services.document_processor import extract_text_from_pdf
from services.chunker import chunk_text


pages = extract_text_from_pdf("sample.pdf")

for page in pages:
    chunks = chunk_text(
        page["text"],
        page["page"]
    )

    print(f"\nPAGE {page['page']}")
    print(f"NUMBER OF CHUNKS: {len(chunks)}")

    for chunk in chunks:
        print(f"\nCHUNK ID: {chunk['chunk_id']}")
        print(f"PAGE: {chunk['page']}")
        print(f"TEXT: {chunk['text']}")

    print("=" * 70)