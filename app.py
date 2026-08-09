from llm_service import LlmService

genai=LlmService()

question = "Explain RAG in  simple terms also tell me what is fine tuning how both are different when to use which and their advance technique."

answer = genai.generate(question)

print(answer)