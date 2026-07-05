import os
import shutil

from models.state import PipelineState


def renderer(state: PipelineState) -> PipelineState:
    """
    Renderer Agent

    Simulates rendering the final Remotion video.
    In production this node will call:

        npx remotion render

    """

    print("=" * 60)
    print("🎬 Renderer Agent Started")
    print("=" * 60)

    if state.status != "compiled":
        print("❌ Script has not been compiled.")
        return state

    os.makedirs("output", exist_ok=True)

    source_script = "output/remotion.tsx"
    final_video = "output/final_video.mp4"

    # Simulation
    with open(final_video, "w") as file:
        file.write(
            "This is a placeholder for the rendered Remotion video."
        )

    state.rendered_video_path = final_video

    state.status = "completed"

    print("✅ Rendering Successful")
    print(f"Video saved at : {final_video}")

    return state