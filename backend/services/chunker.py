def chunk_text(
    text: str,
    page_number: int,
    chunk_size: int = 500,
    overlap: int = 50
):
    chunks = []

    start = 0
    chunk_id = 0

    while start < len(text):

        end = start + chunk_size

        if end < len(text):
            end = text.rfind(" ", start, end)

        if end <= start:
            end = start + chunk_size

        chunk = text[start:end].strip()

        chunks.append({
            "chunk_id": chunk_id,
            "page": page_number,
            "text": chunk
        })

        chunk_id += 1

        start = end - overlap

    return chunks