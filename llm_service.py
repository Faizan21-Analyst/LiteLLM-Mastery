from litellm import completion
from config import GROQ_API_KEY
import os 

os.environ["GROQ_API_KEY"] = GROQ_API_KEY

class LlmService:

    @staticmethod
    def generate(prompt:str):
        response=completion(model="groq/llama-3.3-70b-versatile",
                            messages=[
                                {
                                    'role':'user',
                                    'content':prompt 
                                }
                            ])

        return response.choices[0].message.content
