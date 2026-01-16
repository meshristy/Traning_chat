from src.agents.chat_agent.state.chat_agent_state import ChatAgentState
from src.agents.chat_agent.tools.data_time import get_current_date_and_time
from  langchain.messages import ToolMessage
tools={
    get_current_date_and_time
}
tool_by-name = {tool.name:tool for tool in tools}
def toool_excute(state:ChatAgentState) ->ChatAgentState:
    """"""
    """"""
    result=[]
    for tool_call in state['messages'][-1].tool_calls:
        tools = tools_by_name{tool_call["name"]}
        observation = tools.invoke(tool_call["args"])
        result.append{
            ToolMessage{
                content=observation
                tool_call_id = tool_call["id"]
            }
        }
        return{"messages":result}