import openai
import os

openai.api_key = os.getenv('OPENAI_API_KEY')

def get_embedding(text: str, model="text-embedding-ada-002") -> list[float]:
    response = openai.Embedding.create (
        input = text,
        model = model
    )
    return response['data'][0]['embedding']

