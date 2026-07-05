from unittest.mock import patch, MagicMock
from services.gemini_service import analyze_single_image


@patch("services.gemini_service.Image.open")
@patch("services.gemini_service.client.models.generate_content")
def test_analyze_single_image(mock_generate, mock_open):

    # Mock image opening
    mock_open.return_value = MagicMock()

    # Mock Gemini response
    mock_response = MagicMock()

    mock_response.text = """
{
    "image_name":"test.jpg",
    "description":"Mock Wedding Image",
    "mood":"Happy",
    "quality_score":9.5,
    "importance_score":9.8
}
"""

    mock_generate.return_value = mock_response

    result = analyze_single_image("data/test.jpg")

    assert result.image_name == "test.jpg"
    assert result.description == "Mock Wedding Image"
    assert result.quality_score == 9.5
    assert result.importance_score == 9.8