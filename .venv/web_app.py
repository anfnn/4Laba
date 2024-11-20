import os
from datetime import datetime
import fastapi
from fastapi import HTTPException, FastAPI, Depends, Body, Header
from uvicorn import Config, Server
from model import NoteID, NoteText, NoteInfo, NoteList, NoteCreate

api_router = fastapi.APIRouter()
app = FastAPI()

# Функция для проверки токена
def get_token(authorization: str = Header(None)):
    print(f"Authorization header: {authorization}")  # Отладочное сообщение
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=403, detail="Invalid token format")
    token = authorization.split(" ")[1]
    print(f"Extracted token: {token}")  # Отладочное сообщение
    if not os.path.exists("tokens.txt"):
        with open("tokens.txt", "w") as f:
            f.write("valid_token_123\n")  # Пример допустимого токена
    with open("tokens.txt", "r") as f:
        valid_tokens = f.read().splitlines()
    print(f"Valid tokens: {valid_tokens}")  # Отладочное сообщение
    if token not in valid_tokens:
        raise HTTPException(status_code=403, detail="Invalid token")


@api_router.post("/notes/", response_model=NoteID)
def create_note(text: NoteCreate, authorization: str = Depends(get_token)):
    note_id = len(os.listdir("notes")) + 1
    with open(f"notes/{note_id}.txt", "w") as file:
        file.write(text.text)
    return NoteID(id=note_id)

@api_router.get("/notes/{note_id}", response_model=NoteText)
def read_note(note_id: int, authorization: str = Depends(get_token)):
    try:
        with open(f"notes/{note_id}.txt", "r") as file:
            text = file.read()
        return NoteText(id=note_id, text=text)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Note not found")

@api_router.get("/notes/{note_id}/info", response_model=NoteInfo)
def get_note_info(note_id: int, authorization: str = Depends(get_token)):
    try:
        created_at = datetime.fromtimestamp(os.path.getctime(f"notes/{note_id}.txt"))
        updated_at = datetime.fromtimestamp(os.path.getmtime(f"notes/{note_id}.txt"))
        return NoteInfo(created_at=created_at, updated_at=updated_at)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Note not found")

@api_router.patch("/notes/{note_id}", response_model=NoteID)
def update_note(note_id: int, note: NoteCreate, authorization: str = Depends(get_token)):
    try:
        with open(f"notes/{note_id}.txt", "w") as file:
            file.write(note.text)
        return NoteID(id=note_id)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Note not found")

@api_router.delete("/notes/{note_id}")
def delete_note(note_id: int, authorization: str = Depends(get_token)):
    try:
        os.remove(f"notes/{note_id}.txt")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Note not found")

@api_router.get("/notes/", response_model=NoteList)
def list_notes(authorization: str = Depends(get_token)):
    note_ids = []
    for filename in os.listdir("notes"):
        note_id = int(filename.split(".")[0])
        note_ids.append(note_id)
    return NoteList(notes=note_ids)

# Маршрутизатор
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
