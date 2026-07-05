from typing import List, Optional
from pydantic import BaseModel, Field

from models.analysis import ImageAnalysis
from models.intent import VideoIntent


class PipelineState(BaseModel):
    # User Input
    user_prompt: str

    # Images
    image_paths: List[str] = Field(default_factory=list)
    image_analysis: List[ImageAnalysis] = Field(default_factory=list)
    selected_images: List[str] = Field(default_factory=list)

    # Intent
    video_intent: Optional[VideoIntent] = None

    # RAG Context
    style_context: str = ""
    remotion_context: str = ""

    # Storyboard
    storyboard: Optional[dict] = None

    # Generated Script
    remotion_script: Optional[str] = None

    # Compiler
    compile_errors: List[str] = Field(default_factory=list)
    retry_count: int = 0

    # Final Output
    rendered_video_path: Optional[str] = None

    # Pipeline Status
    status: str = "initialized"