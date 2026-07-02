from PIL import Image
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def analyze_single_image(image_path: str):
    image = Image.open(image_path)

    print(f"Image Size: {image.size}")
    print(f"Image Mode: {image.mode}")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            "Describe this image in one sentence.",
            image
        ]
    )

    print(response.text)


def test_connection():
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Reply with exactly: Gemini Connected"
    )

    return response.text