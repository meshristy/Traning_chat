from fastapi import APIRouter
from src.handlers.Chat_handler import Chat_handler
from langchain.messages import AnyMessage
from src.agents.chat_agent.state.chat_agent_state import ChatAgentState
router = APIRouter()
@router.post ("/chat")
def chat_with_ai(message :str) -> ChatAgentState:
    """"""
    
    """"""
    return Chat_handler(message=message)