from models.state import PipelineState


def test_pipeline_state():

    from models.state import PipelineState

def test_pipeline_state():

    state = PipelineState(
        user_prompt="Create a cinematic wedding video."
    )

    assert state.user_prompt == "Create a cinematic wedding video."

    assert state is not None