import json
import os

from models.state import PipelineState


class OutputService:

    @staticmethod
    def save_pipeline_state(state: PipelineState):

        os.makedirs("output", exist_ok=True)

        with open(
            "output/pipeline_state.json",
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                state.model_dump(),
                file,
                indent=4,
                ensure_ascii=False
            )

        print("✅ pipeline_state.json saved.")

    @staticmethod
    def save_storyboard(state: PipelineState):

        if not state.storyboard:
            return

        os.makedirs("output", exist_ok=True)

        with open(
            "output/storyboard.json",
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                state.storyboard,
                file,
                indent=4,
                ensure_ascii=False
            )

        print("✅ storyboard.json saved.")