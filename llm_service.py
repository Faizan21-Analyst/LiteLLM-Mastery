from litellm import completion
from config import GROQ_API_KEY , PRIMARY_MODEL,FALLBACK_MODEL,GEMINI_API_KEY
import os 
from router import choose,Request

os.environ["GEMINI_API_KEY"] = GEMINI_API_KEY
os.environ['GROQ_API_KEY'] = GROQ_API_KEY


class LlmService():
    
    @staticmethod
    def generate(prompt:str):
        request_data=Request(prompt=prompt, primary_model=PRIMARY_MODEL, fallback_model=FALLBACK_MODEL)


        choose_model=choose(request_data)
        try:
            response=completion(model=choose_model,
                                messages=[
                                    {
                                        'role':'user',
                                        'content':prompt 
                                    }
                                ])

            return response.choices[0].message.content 
        
        except Exception as e:

            print(f"Primary model failed: {e}")
            print("Trying fallback model...")

            response = completion(
                model=FALLBACK_MODEL,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            return response.choices[0].message.content
