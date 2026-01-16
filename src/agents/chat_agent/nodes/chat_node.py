from src.agents.chat_agent.state.chat_agent_state import ChatAgentState
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
from src.agents.chat_agent.tools.data_time import get_current_date_and_time
load_dotenv(override=True)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
def chat(state:ChatAgentState) -> ChatAgentState:
    """"""
    """"""
    model = ChatGroq(
        model = "llama-3.1-8b-instant",
        api_key = GROQ_API_KEY
    )
    model = model.bind_tools([get_current_date_and_time])
    tools={
        get_current_date_and_time
    }
    answer = model.invoke(state["messages"])
    return{
        "messages":[answer]
    }