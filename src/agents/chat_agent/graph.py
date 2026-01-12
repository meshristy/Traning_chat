from src.agents.chat_agent.state.chat_agent_state import chatAgentState
from src.agents.chat_agent.nodes.chat_node import chat
from langgraph.graph import START,END ,StateGraph
from langgraph.graph.state import CompiledStateGraph
def create_chat_agent_graph() ->CompiledStateGraph:
    """"""
    """"""
    graph_builder = StateGraph(chatAgentState)
    graph_builder.add_node("chat_node",chat)
    graph_builder.add_edge(START,"chat_node")
    graph_builder.add_edge("Chat_node",END)
    return graph_builder.compile()