from services.document_processor import extract_text_from_pdf

pages = extract_text_from_pdf("sample.pdf")

for page in pages:
    print("PAGE:", page["page"])
    print(page["text"])
    print("-" * 50)