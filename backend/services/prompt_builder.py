def build_prompt(query: str, results):

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    context = ""

    for i, document in enumerate(documents):

        page = metadatas[i]["page"]

        context += f"""
SOURCE {i + 1} - PAGE {page}

{document}

"""

    prompt = f"""
You are a CV question-answering assistant.

Answer the question using ONLY the context.

The context contains project entries. Each project entry starts with its PROJECT TITLE.

IMPORTANT:
- Return the actual project titles, not technologies, features, techniques, or descriptions.
- A project title is the text at the beginning of a project entry.
- Do NOT turn sentences beginning with "Developed", "Built", "Implemented", or "Integrated" into project names.
- Do NOT return technology names such as AI-Based Recommendation System, Random Forest, FAISS, AWS Lambda, or Anomaly Detection.
- If the question asks for machine learning projects, identify the projects that use machine learning, AI, NLP, predictive models, or related techniques.
- Return only the project titles.
- Do not invent project names.

The project titles appearing in the context are:

1. Urban Water Quality Prediction Using Ubiquitous Data
2. QueryTube – AI-Powered Semantic Video Search & Summarization System
3. Agri AI – Smart Agriculture Intelligence & Marketplace Platform
4. Observability and Event Intelligence Pipeline

QUESTION:
{query}

CONTEXT:
{context}

ANSWER:
"""

    return prompt