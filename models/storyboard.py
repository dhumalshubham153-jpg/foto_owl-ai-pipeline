from pydantic import BaseModel
from typing import List


class Scene(BaseModel):
    scene_number: int

    image_name: str

    image_path: str

    duration: int

    caption: str

    transition: str


class Storyboard(BaseModel):
    title: str
    total_duration: int
    scenes: List[Scene]