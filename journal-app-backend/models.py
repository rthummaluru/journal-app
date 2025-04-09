from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import Text
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Entry(Base):
    __tablename__ = "entries"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(Text, index=True)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    
    