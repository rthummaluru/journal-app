import openai
import os
from typing import List
from dotenv import load_dotenv

load_dotenv()

# Initialize the OpenAI client
client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def get_embedding(text: str, model="text-embedding-ada-002") -> List[float]:
    response = client.embeddings.create (
        input = [text],
        model = model
    )
    return response.data[0].embedding

