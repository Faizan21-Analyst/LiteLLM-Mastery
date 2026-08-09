from llm_service import LlmService

genai=LlmService()

question = "Explain RAG in GENAI simple terms."

answer = genai.generate(question)

print(answer)