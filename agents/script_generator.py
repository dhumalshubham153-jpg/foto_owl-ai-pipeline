import os

from models.state import PipelineState
from services.chroma_service import ChromaService


def script_generator(state: PipelineState) -> PipelineState:
    """
    Script Generator Agent

    Generates a Remotion TSX composition using the storyboard
    and Remotion documentation retrieved from ChromaDB.
    """

    print("=" * 60)
    print("🎥 Script Generator Started")
    print("=" * 60)

    # -----------------------------
    # Retrieve Remotion Documentation
    # -----------------------------
    rag = ChromaService()

    query = f"{state.video_intent.video_style} Sequence Component"

    remotion_context = rag.search_remotion(query)

    state.remotion_context = remotion_context

    print("\n📖 Retrieved Remotion Documentation:\n")
    print(remotion_context)
    print("-" * 60)

    storyboard = state.storyboard

    if not storyboard:
        raise ValueError("Storyboard not found. Script generation cannot continue.")

    code = f"""
/*
=========================================
Retrieved Style Guide
=========================================

{state.style_context}

=========================================
Retrieved Remotion Context
=========================================

{state.remotion_context}

=========================================
Generated Remotion Composition
=========================================
*/

import {{ AbsoluteFill, Img, Sequence }} from "remotion";

export const WeddingVideo = () => (
  <AbsoluteFill>

    <Sequence from={{0}} durationInFrames={{150}}>

      <Img
        src="./images/{storyboard['scenes'][0]['image_name']}.jpg"
        style={{{{
          width: "100%",
          height: "100%",
          objectFit: "cover"
        }}}}
      />

    </Sequence>

  </AbsoluteFill>
);
"""

    # Save in Pipeline State
    state.remotion_script = code

    # Save generated TSX file
    os.makedirs("output", exist_ok=True)

    with open("output/remotion.tsx", "w", encoding="utf-8") as file:
        file.write(code)

    print("✅ Remotion script saved to output/remotion.tsx")

    state.status = "script_generated"

    print("✅ Script Generator Completed")

    return state