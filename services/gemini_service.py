import json
import os
from pathlib import Path

from PIL import Image
from dotenv import load_dotenv
from google import genai

from models.analysis import ImageAnalysis

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_single_image(image_path: str) -> ImageAnalysis:
    """
    Analyze a single image using Gemini Vision.
    """

    image = Image.open(image_path)

    prompt = """
You are an expert image analyst.

Return ONLY valid JSON.

{
    "image_name": "",
    "description": "",
    "mood": "",
    "quality_score": 0.0,
    "importance_score": 0.0
}

Do NOT include image_path.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                prompt,
                image
            ]
        )

        text = response.text.strip()
        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

        data = json.loads(text)

        data["image_path"] = image_path

        return ImageAnalysis(**data)

    except Exception as e:

        print("=" * 60)
        print("Gemini API unavailable.")
        print(e)
        print("Using fallback analysis...")
        print("=" * 60)

        filename = Path(image_path).name

        return ImageAnalysis(
            image_name=filename,
            image_path=image_path,
            description="Fallback image analysis because Gemini service is unavailable.",
            mood="Neutral",
            quality_score=0.85,
            importance_score=0.80
        )


def analyze_image_batch(image_paths: list[str]) -> list[ImageAnalysis]:
    """
    Analyze multiple images using ONE Gemini API call.
    """

    prompt = """
You are an expert wedding photo selector.

You will receive multiple wedding images.

Compare ALL images together.

For EACH image return:

- image_name
- description (2-3 sentences)
- mood
- quality_score (0-10)
- importance_score (0-10)

IMPORTANT:
- Compare images against each other.
- Use the full score range.
- Rank stronger images higher.
- Return ONE JSON object per image.

Return ONLY valid JSON array.

Example:

[
  {
    "image_name":"AHD_6008.jpg",
    "description":"Bride smiling during ceremony.",
    "mood":"Emotional",
    "quality_score":9.2,
    "importance_score":9.8
  }
]
"""

    contents = [prompt]

    for image_path in image_paths:
        contents.append(Image.open(image_path))

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=contents
        )

        text = response.text.strip()

        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

        data = json.loads(text)

        analyses = []

        for item, image_path in zip(data, image_paths):

            item["image_path"] = image_path

            analyses.append(
                ImageAnalysis(**item)
            )

        return analyses

    except Exception as e:

        print("=" * 60)
        print("Batch Analysis Failed")
        print(e)
        print("Falling back to single-image analysis...")
        print("=" * 60)

        analyses = []

        for image_path in image_paths:
            analyses.append(
                analyze_single_image(image_path)
            )

        return analyses


def test_connection():

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Reply exactly: Gemini Connected"
        )

        return response.text

    except Exception as e:

        return f"Connection Failed: {e}"