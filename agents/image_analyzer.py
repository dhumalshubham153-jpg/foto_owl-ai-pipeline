from models.state import PipelineState


def image_analyzer(state: PipelineState) -> PipelineState:
    print("Image Analyzer Started")

    # We will replace this with Gemini later
    state.status = "images_analyzed"

    return state