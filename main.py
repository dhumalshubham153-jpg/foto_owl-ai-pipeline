from pathlib import Path

from graph.builder import graph
from models.state import PipelineState
from services.output_services import OutputService


def load_images(folder="public/images"):
    supported_extensions = {".jpg", ".jpeg", ".png"}

    image_paths = [
        str(path)
        for path in Path(folder).iterdir()
        if path.suffix.lower() in supported_extensions
    ]

    return sorted(image_paths)


image_paths = load_images()

print(f"\n📂 Found {len(image_paths)} images.\n")

state = PipelineState(
    user_prompt="Create a cinematic wedding reel with emotional music",
    image_paths=image_paths
)

result = graph.invoke(state)

print("\n========== FINAL PIPELINE STATE ==========\n")
print(result)

final_state = PipelineState(**result)

OutputService.save_pipeline_state(final_state)
OutputService.save_storyboard(final_state)