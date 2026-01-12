from src.agents.chat_agent.graph import create_chat_agent_graph



def chat_handler(message :str) -> dict[str,str]:
    """
    Recives a message from user and sets it after motification 

    Args:
        message (str): The user message
    Returns:
        dict[str,str]:  Modified message
    """ 
    graph = create_chat_agent_graph()
    return{"message":graph.invoke([message])}