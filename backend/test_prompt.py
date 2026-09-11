from services.retriever import search_documents
from services.prompt_builder import build_prompt
from services.llm_service import generate_answer


query = "What machine learning projects did I work on?"


results = search_documents(
    query,
    top_k=5
)


prompt = build_prompt(
    query,
    results
)


answer = generate_answer(
    prompt
)


print("\nQUESTION:")
print(query)

print("\nANSWER:")
print(answer)