from pydantic import BaseModel


class VideoIntent(BaseModel):
    video_style: str
    mood: str
    pacing: str
    transition: str
    duration: int
    music_style: str