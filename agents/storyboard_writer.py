from models.state import PipelineState
from models.storyboard import Storyboard, Scene
from services.chroma_service import ChromaService


def storyboard_writer(state: PipelineState) -> PipelineState:
    """
    Storyboard Writer Agent

    Uses the retrieved style guide from ChromaDB to
    generate a storyboard based on the selected images.
    """

    print("=" * 60)
    print("🎬 Storyboard Writer Started")
    print("=" * 60)

    # Initialize RAG
    rag = ChromaService()

    # Retrieve style guide
    style_context = rag.search_style(
        state.video_intent.video_style
    )

    state.style_context = style_context

    print("\n📖 Retrieved Style Guide:\n")
    print(style_context)
    print("-" * 60)

    scenes = []

    # Use only selected images
    selected_images = [
        image
        for image in state.image_analysis
        if image.image_name in state.selected_images
    ]

    for index, image in enumerate(selected_images):

        scene = Scene(
            scene_number=index + 1,
            image_name=image.image_name,
            image_path=image.image_path,
            duration=5,
            caption=image.description,
            transition=state.video_intent.transition
        )

        scenes.append(scene)

    storyboard = Storyboard(
        title=f"{state.video_intent.video_style} Storyboard",
        total_duration=len(scenes) * 5,
        scenes=scenes
    )

    state.storyboard = storyboard.model_dump()

    state.status = "storyboard_generated"

    print("✅ Storyboard Generated Successfully")
    print(f"Scenes Created: {len(scenes)}")
    print(storyboard)

    return state