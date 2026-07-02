from langgraph.graph import StateGraph

from models.state import PipelineState
from agents.image_analyzer import image_analyzer

def start_node(state: PipelineState):
    print("Pipeline Started")
    state.status = "started"
    return state


builder = StateGraph(PipelineState)

builder.add_node("start", start_node)
builder.add_node("image_analyzer",image_analyzer)
builder.add_edge("start","image_analyzer")
builder.set_entry_point("start")

builder.set_finish_point("image_analyzer")

graph = builder.compile()