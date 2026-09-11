from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from services.document_processor import extract_text_from_pdf
from services.retriever import search_documents
from services.prompt_builder import build_prompt
from services.llm_service import generate_answer

import os

app = FastAPI(title="Document QA API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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
class QuestionRequest(BaseModel):
    question: str


@app.post("/ask")
async def ask_question(request: QuestionRequest):

    results = search_documents(
        request.question,
        top_k=5
    )

    prompt = build_prompt(
        request.question,
        results
    )

    answer = generate_answer(
        prompt
    )

    return {
        "question": request.question,
        "answer": answer
    }