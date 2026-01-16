from fastapi import APIRouter
from src.handlers.Chat_handler import Chat_handler, chat_history_handler, get_all_threads

router = APIRouter()

@router.post("/chat/{thread_id}")
def chat_with_ai(thread_id: str, message: str):
    return Chat_handler(thread_id=thread_id, message=message)

@router.get("/chat/history/{thread_id}")
def get_chat_history(thread_id: str):
    return chat_history_handler(thread_id=thread_id)

@router.get("/chat/threads")
def get_threads():
    return get_all_threads()
