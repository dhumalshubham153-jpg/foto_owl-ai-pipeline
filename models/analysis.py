from pydantic import BaseModel


class ImageAnalysis(BaseModel):
    image_name: str
    description: str
    mood: str
    quality_score: float
    importance_score: float