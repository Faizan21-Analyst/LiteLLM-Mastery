from config import GEMINI_API_KEY,GROQ_API_KEY,PRIMARY_MODEL,FALLBACK_MODEL
from pydantic import BaseModel,Field
import logging
logger = logging.getLogger("app.router")
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class Request(BaseModel):
    prompt: str = Field(..., description="The user prompt text to analyze")
    primary_model: str = Field(default=PRIMARY_MODEL)
    fallback_model: str = Field(default=FALLBACK_MODEL)

def choose(data:Request):
    try:
        word_count=len(data.prompt.split())

        if word_count>20:
            selected_model= data.primary_model
        else:
            selected_model= data.fallback_model

        logger.info(
            f"Routing Decision | Word Count: {word_count} | Selected Model: {selected_model}"
        )

        return selected_model
    except Exception as e:
        logger.error(f"Routing failed due to unexpected error: {str(e)}. Falling back to primary.")
        return data.primary_model