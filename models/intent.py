from typing import Optional
from pydantic import BaseModel


class VideoIntent(BaseModel):
    pacing: Optional[str] = None
    visual_style: Optional[str] = None
    caption_tone: Optional[str] = None
    transition_preference: Optional[str] = None