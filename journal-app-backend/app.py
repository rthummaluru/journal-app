from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from models import Entry as DBEntry
from database import get_db
import uvicorn
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi.middleware.cors import CORSMiddleware
from embeddings import get_embedding
from vector_store import VectorStore
import openai
from fastapi import HTTPException
import os
from dotenv import load_dotenv 

load_dotenv()

# Create a FastAPI instance
app = FastAPI()

# Create a vector store instance
store = VectorStore()

openai.api_key = os.getenv("OPENAI_API_KEY")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Define a Pydantic model for the entry
class JournalEntry(BaseModel):
    title: str
    body: str

class QuestionInput(BaseModel):
    question: str

# Define a root endpoint
@app.post("/entries")
def new_entry(entry: JournalEntry):
    db = next(get_db())
    db_entry = DBEntry(title=entry.title, body=entry.body)
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)

    # Create an embedding for the entry
    entry_text = f"{db_entry.title}\n{db_entry.body}"
    entry_embedding = get_embedding(entry_text)
    store.add(entry_text, entry_embedding)

    return db_entry

# A get endpoint to get all entries
@app.get("/entries")
def get_entries(db: Session = Depends(get_db)):
    entries = db.query(DBEntry).order_by(DBEntry.created_at.desc()).all()
    return [
        {
            "id": entry.id,
            "title": entry.title,
            "body": entry.body,
            "created_at": entry.created_at,
            "updated_at": entry.updated_at,
        }
        for entry in entries
    ]

@app.post("/ask-ai")
def user_query(user_input: QuestionInput, db: Session = Depends(get_db)):
    entries = db.query(DBEntry).order_by(DBEntry.created_at.desc()).all()
    entry_texts = [entry.body for entry in entries]
    
    for text in entry_texts:
        embedding = get_embedding(text)
        store.add(text, embedding)
    
    query_embedding = get_embedding(user_input.question)
    relevant_entries = store.search(query_embedding, k=5)

    prompt = f""""You are an introspective journal assistant. Here are some past journal entries:
            {chr(10).join(relevant_entries)}
            Now answer this question based on the entries above:
            {user_input.question}
            """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return {"answer": response['choices'][0]['message']['content']}


    


# This is just to make sure the file is properly saved
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)