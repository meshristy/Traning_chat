from fastapi import APIRouter
from src.handlers.Chat_handler import chat_handler
router = APIRouter()
@router.post ("/chat")
def chat_with_ai(message :str) -> dict[str,str]:
    """"""
    
    """"""
    return chat_handler(message=message)