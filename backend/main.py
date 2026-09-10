from fastapi import FastAPI, UploadFile, File
from services.document_processor import extract_text_from_pdf
import os


app = FastAPI(title="Document QA API")


@app.get("/")
def home():
    return {
        "message": "Document QA API is running"
    }


@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    file_path = os.path.join("uploads", file.filename)

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    pages = extract_text_from_pdf(file_path)

    return {
        "filename": file.filename,
        "pages": pages
    }