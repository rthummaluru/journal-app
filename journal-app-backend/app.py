from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import uvicorn

# Create a FastAPI instance
app = FastAPI()

# Define a Pydantic model for the entry
class Entry(BaseModel):
    title: str
    date: datetime
    body: str

# Define a root endpoint
@app.post("/entries")
def new_entry(entry: Entry):
    # Store entries in a list (note: this will reset when server restarts)
    if not hasattr(app, "entries"):
        app.entries = []
    
    # Add the new entry to the list
    app.entries.append(entry)
    
    # Return all entries
    return app.entries

# This is just to make sure the file is properly saved
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)