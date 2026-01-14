from src.agents.chat_agent.graph import create_chat_agent_graph
from langchain.messages import HumanMessage,AnyMessage
from src.agents.chat_agent.state.chat_agent_state import ChatAgentState


def Chat_handler(message :str) -> ChatAgentState:
    """
    Recives a message from user and sets it after motification 

    Args:
        message (str): The user message
    Returns:
        dict[str,str]:  Modified message
    """ 
    graph = create_chat_agent_graph()
    return graph.invoke(
        input={
            "messages":[HumanMessage(content=message)]
        },
        config={
            "configurable":{
                 "thread_id":"1"
            }
           
        }
    )
 