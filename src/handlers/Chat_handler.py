from src.agents.chat_agent.graph import create_chat_agent_graph
from langchain.messages import HumanMessage, AnyMessage
from src.agents.chat_agent.state.chat_agent_state import ChatAgentState

graph = create_chat_agent_graph()

# ------------------ CHAT ------------------

def Chat_handler(thread_id: str, message: str):
    return graph.invoke(
        input={
            "messages": [HumanMessage(content=message)]
        },
        config={
            "configurable": {
                "thread_id": thread_id
            }
        }
    )


# ------------------ THREAD LIST ------------------

def get_all_threads():
    checkpoints = graph.checkpointer.list(config={})
    threads = set()

    for cp in checkpoints:
        if "configurable" in cp.config and "thread_id" in cp.config["configurable"]:
            threads.add(cp.config["configurable"]["thread_id"])

    return list(threads)


# ------------------ CHAT HISTORY ------------------

def chat_history_handler(thread_id: str):
    checkpoint = graph.checkpointer.get(
        config={
            "configurable": {
                "thread_id": thread_id
            }
        }
    )

    if not checkpoint:
        return {"messages": []}

    return {"messages": checkpoint["channel_values"]["messages"]}
