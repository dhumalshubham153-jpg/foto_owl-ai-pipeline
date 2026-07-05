from langgraph.graph import StateGraph, END
from agents.storyboard_writer import storyboard_writer
from agents.script_generator import script_generator
from models.state import PipelineState

from agents.intent_parser import intent_parser
from agents.image_analyzer import image_analyzer
from agents.compiler import compiler
from agents.renderer import renderer

def start_node(state: PipelineState):
    print("=" * 60)
    print("🚀 Pipeline Started")
    print("=" * 60)

    state.status = "started"
    return state

def should_retry(state: PipelineState):

    if state.status == "retry":
        return "script_generator"

    if state.status == "failed":
        return END

    return "renderer"


builder = StateGraph(PipelineState)

# Nodes
builder.add_node("start", start_node)
builder.add_node("intent_parser", intent_parser)
builder.add_node("image_analyzer", image_analyzer)
builder.add_node("storyboard_writer", storyboard_writer)
builder.add_node("script_generator", script_generator)
builder.add_node("compiler", compiler)
builder.add_node("renderer", renderer)

# Flow
builder.set_entry_point("start")

builder.add_edge("start", "intent_parser")
builder.add_edge("intent_parser", "image_analyzer")
builder.add_edge("image_analyzer", "storyboard_writer")
builder.add_edge("storyboard_writer", "script_generator")
builder.add_edge("script_generator", "compiler")
builder.add_conditional_edges(
    "compiler",
    should_retry
)

builder.set_finish_point("renderer")

graph = builder.compile()