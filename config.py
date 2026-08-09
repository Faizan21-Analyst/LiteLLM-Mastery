from dotenv import load_dotenv
load_dotenv()
import os 

GROQ_API_KEY=os.getenv("GROQ_API_KEY")
PRIMARY_MODEL=os.getenv("PRIMARY_MODEL")
FALLBACK_MODEL=os.getenv('FALLBACK_MODEL')
GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is missing! Check your environment variables or .env file.")

