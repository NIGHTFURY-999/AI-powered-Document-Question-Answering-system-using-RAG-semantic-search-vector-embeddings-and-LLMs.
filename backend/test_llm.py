from services.llm_service import generate_answer


prompt = """
Explain what Random Forest is in two simple sentences.
"""


answer = generate_answer(prompt)


print("LLM ANSWER:")
print(answer)