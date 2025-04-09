from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from models import Entry as DBEntry
from database import get_db
import uvicorn

# Create a FastAPI instance
app = FastAPI()

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

# This is just to make sure the file is properly saved
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)