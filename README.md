# AI-Powered Document Question Answering System

A Retrieval-Augmented Generation (RAG) based document question-answering system that allows users to ask natural-language questions about documents and receive context-aware answers.

The system combines semantic search, vector embeddings, ChromaDB, and a locally running LLM through Ollama to retrieve relevant document information before generating an answer.

---
## 💡 Why I Built This Project

I built this project to understand how modern AI-powered document question-answering systems work internally.

Instead of relying on a simple keyword search or sending an entire document directly to an LLM, I wanted to build a complete Retrieval-Augmented Generation (RAG) pipeline from the ground up.

The project helped me understand how:

- Documents can be converted into searchable semantic representations.
- Vector embeddings can be used to find information based on meaning rather than exact keywords.
- Vector databases such as ChromaDB can store and retrieve relevant document chunks.
- Retrieved context can be provided to an LLM to generate grounded answers.
- Local LLMs can be integrated into an application without depending on paid external APIs.
- A Python AI backend can be connected to a modern Next.js frontend through REST APIs.

The project was also designed as a practical way to strengthen my understanding of Generative AI, RAG architectures, semantic search, vector databases, and full-stack AI application development.

## 🧩 Challenges Faced & Solutions

Building the system involved several practical challenges that helped me understand the limitations and engineering decisions involved in RAG systems.

### 1. PDF Text Extraction and Layout

**Challenge:**  
PDFs do not always preserve their original visual structure when text is extracted. Headings, paragraphs, and sections can sometimes appear in an unexpected order or formatting.

**Solution:**  
Used PyMuPDF to extract text while retaining page information and developed document-aware processing logic for structured content.

---

### 2. Choosing an Appropriate Chunking Strategy

**Challenge:**  
Initially, the document was divided into fixed-size chunks. This caused unrelated sections of the CV to appear in the same chunk, such as projects being mixed with skills or internship information.

**Solution:**  
Implemented project-aware chunking that identifies project titles and keeps each project together with its description, technology stack, and impact.

This significantly improved the quality of semantic retrieval.

---

### 3. Improving Retrieval Quality

**Challenge:**  
The first retrieval results contained fragmented information and sometimes returned parts of multiple sections together.

**Solution:**  
Inspected the retrieved chunks and redesigned the chunking strategy before generating new embeddings and rebuilding the ChromaDB collection.

This demonstrated an important RAG principle:

> Better retrieval starts with better document representation.

---

### 4. Working with a Small Local LLM

**Challenge:**  
The project was designed to run locally without relying on paid LLM APIs. The available hardware limited the size of the model that could be comfortably used.

**Solution:**  
Used Ollama with Gemma 3 1B for local inference.

The smaller model reduced hardware requirements but also introduced occasional limitations in interpreting complex retrieved context.

---

### 5. Preventing Incorrect Answers

**Challenge:**  
The LLM could sometimes interpret descriptions, technologies, or features as project names.

For example, a statement such as:

```text
Developed an AI-powered recommendation system


## 🚀 Features

- 📄 PDF document text extraction
- ✂️ Semantic/project-aware document chunking
- 🔢 Sentence Transformer embeddings
- 🗄️ Persistent ChromaDB vector database
- 🔍 Semantic similarity search
- 🤖 Retrieval-Augmented Generation (RAG)
- 🧠 Local LLM inference using Ollama
- ⚡ FastAPI backend
- 🎨 Next.js frontend
- 🔗 REST API communication between frontend and backend
- 🌐 CORS configuration for frontend-backend communication
- 💻 Fully local AI inference without paid LLM APIs

---

## 🏗️ System Architecture

```text
                    ┌──────────────────────┐
                    │      PDF Document    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Text Extraction    │
                    │       PyMuPDF        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      Chunking        │
                    │ Semantic Chunks      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     Embeddings       │
                    │ Sentence Transformers│
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      ChromaDB        │
                    │    Vector Store      │
                    └──────────┬───────────┘
                               │
                         User Question
                               │
                               ▼
                    ┌──────────────────────┐
                    │      Retrieval       │
                    │ Semantic Search      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Prompt Builder    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Ollama + Gemma     │
                    │       Local LLM      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    FastAPI /ask      │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Next.js UI        │
                    └──────────────────────┘
🛠️ Tech Stack
Backend
Python
FastAPI
PyMuPDF
Sentence Transformers
ChromaDB
Requests
AI / Machine Learning
Retrieval-Augmented Generation (RAG)
Semantic Search
Vector Embeddings
Sentence Transformers
Ollama
Gemma 3 1B
Frontend
Next.js
React
TypeScript
Tailwind CSS
Development Tools
Git
GitHub
PowerShell
Virtual Environment (venv)
📂 Project Structure
document-QA/
│
├── backend/
│   │
│   ├── main.py
│   │
│   ├── services/
│   │   ├── document_processor.py
│   │   ├── chunker.py
│   │   ├── embedding_service.py
│   │   ├── vector_store.py
│   │   ├── retriever.py
│   │   ├── prompt_builder.py
│   │   └── llm_service.py
│   │
│   ├── test_processor.py
│   ├── test_chunker.py
│   ├── test_embedding.py
│   ├── test_ingestion.py
│   ├── test_vector_store.py
│   ├── test_retrieval.py
│   ├── test_prompt.py
│   └── test_llm.py
│
├── frontend/
│   │
│   ├── app/
│   │   ├── page.tsx
│   │   ├── layout.tsx
│   │   └── globals.css
│   │
│   ├── package.json
│   └── ...
│
├── .gitignore
└── README.md
⚙️ How It Works
1. Document Processing

PDF documents are processed using PyMuPDF to extract their text and page information.

PDF → Text + Page Metadata
2. Chunking

The extracted text is divided into meaningful semantic units.

For structured documents such as CVs, project-level chunks are preserved.

Project
 ├── Description
 ├── Technology Stack
 └── Impact
3. Embeddings

Each chunk is converted into a numerical vector using:

all-MiniLM-L6-v2

The model produces a 384-dimensional embedding representing the semantic meaning of the text.

4. Vector Storage

The embeddings and their corresponding text are stored in ChromaDB.

Text Chunk
    ↓
Embedding
    ↓
ChromaDB
5. Retrieval

When a user asks a question, the question is converted into an embedding.

ChromaDB then searches for the most semantically similar document chunks.

Lower vector distance indicates greater semantic similarity.

6. Prompt Construction

The retrieved document chunks are inserted into a prompt together with the user's question.

The LLM is instructed to answer using the retrieved context.

7. Local LLM Generation

Ollama runs Gemma locally and generates the final answer.

This avoids requiring a paid external LLM API.

🔌 API
Ask a Question

Endpoint

POST /ask

Request

{
  "question": "What machine learning projects did I work on?"
}

Response

{
  "question": "What machine learning projects did I work on?",
  "answer": "..."
}
API Documentation

When the backend is running, interactive FastAPI documentation is available at:

http://127.0.0.1:8000/docs
💻 Running Locally
Prerequisites

Install:

Python 3.13+
Node.js
npm
Ollama
1. Clone the repository
git clone https://github.com/NIGHTFURY-999/AI-powered-Document-Question-Answering-system-using-RAG-semantic-search-vector-embeddings-and-LLMs.git
cd AI-powered-Document-Question-Answering-system-using-RAG-semantic-search-vector-embeddings-and-LLMs
2. Backend Setup

Navigate to the backend:

cd backend

Create a virtual environment:

python -m venv venv

Activate it:

.\venv\Scripts\Activate.ps1

Install dependencies:

pip install fastapi uvicorn python-multipart pymupdf python-docx
pip install sentence-transformers
pip install chromadb
3. Install and Run Ollama

Install Ollama and download the model:

ollama pull gemma3:1b

Start the backend:

python -m uvicorn main:app

The API will run at:

http://127.0.0.1:8000
4. Frontend Setup

Open another terminal:

cd frontend

Install dependencies:

npm install

Start the development server:

npm run dev

Open:

http://localhost:3000
🧪 Example
User Question
What machine learning projects did I work on?
RAG Pipeline
Question
   ↓
Question Embedding
   ↓
ChromaDB Semantic Search
   ↓
Relevant Project Chunks
   ↓
Prompt Construction
   ↓
Gemma 3 1B
   ↓
Generated Answer
🎯 Learning Outcomes

This project was developed to understand the practical implementation of Retrieval-Augmented Generation rather than relying on a pre-built chatbot framework.

Key concepts implemented:

Document ingestion
Text preprocessing
Semantic chunking
Vector embeddings
Vector databases
Similarity search
Retrieval pipelines
Prompt engineering
Local LLM inference
REST API development
Frontend/backend integration
🔮 Future Improvements

Planned improvements include:

 Multi-document upload
 DOCX support through the frontend
 Source/page citations
 Improved no-answer detection
 Conversation history
 Document preview
 Better section-aware metadata
 Stronger local or hosted LLM
 RAG evaluation metrics
 Production deployment
 User authentication
 Document management
⚠️ Current Limitations

This is currently a Version 1 RAG prototype.

The current implementation is optimized around structured document/project content and uses a small local 1B parameter LLM. As a result, some complex questions may occasionally produce incomplete or imperfect answers.

Future versions will improve retrieval filtering, metadata, answer validation, and model quality.

👨‍💻 Author

Vaibhav Haldankar

MCA — Artificial Intelligence / Data Science

Interested in:

Artificial Intelligence
Machine Learning
Data Science
Generative AI
Backend Development
RAG Systems
⭐ Project

If you found this project useful, consider giving the repository a ⭐.


### One important correction before you commit

I deliberately called the current version a **"Version 1 RAG prototype"** rather than claiming that it is a production-ready document QA system. That's more credible in an interview because we actually tested its limitations.

Now save `README.md` in the **root**:

```text
document-QA/
└── README.md
