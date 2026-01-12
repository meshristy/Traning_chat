from src.agents.chat_agent.state.chat_agent_state import chatAgentState
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
load_dotenv(override=True)
GROQ_API_KEY = os.getenv(" GROQ_API_KEY")
def chat(state:chatAgentState) -> chatAgentState:
    """"""
    """"""
    model = ChatGroq(
        model = " ",
        api_key = GROQ_API_KEY
    )
    return{
        "messages":model.invoke([state["messages"]]).content
    }