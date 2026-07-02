from graph.builder import graph
from models.state import PipelineState

state = PipelineState(
    user_prompt="Cinematic wedding reel"
)

result = graph.invoke(state)

print(result)