from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from models import Entry as DBEntry
from database import get_db
import uvicorn
from sqlalchemy.orm import Session
from fastapi import Depends
from fastapi.middleware.cors import CORSMiddleware


# Create a FastAPI instance
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ← you can change this to ["http://localhost:5173"] for stricter control
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Define a Pydantic model for the entry
class JournalEntry(BaseModel):
    title: str
    body: str

# Define a root endpoint
@app.post("/entries")
def new_entry(entry: JournalEntry):
    db = next(get_db())
    db_entry = DBEntry(title=entry.title, body=entry.body)
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
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

# This is just to make sure the file is properly saved
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)