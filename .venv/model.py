from pydantic import BaseModel
from datetime import datetime
from typing import List

class NoteCreate(BaseModel):
    text: str

class NoteInfo(BaseModel):
    created_at: datetime
    updated_at: datetime

class NoteText(BaseModel):
    id: int
    text: str

class NoteID(BaseModel):
    id: int

class NoteList(BaseModel):
    notes: List[int]

