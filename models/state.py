from typing import List, Optional
from pydantic import BaseModel

from models.analysis import ImageAnalysis
from models.intent import VideoIntent


class PipelineState(BaseModel):
    user_prompt: str

    image_paths: List[str] = []

    video_intent: Optional[VideoIntent] = None

    image_analysis: List[ImageAnalysis] = []

    selected_images: List[str] = []

    storyboard: Optional[dict] = None

    remotion_script: Optional[str] = None

    compile_errors: List[str] = []

    retry_count: int = 0

    rendered_video_path: Optional[str] = None

    status: str = "started"