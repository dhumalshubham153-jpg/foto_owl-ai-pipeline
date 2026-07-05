from models.analysis import ImageAnalysis


def test_image_analysis():

    image = ImageAnalysis(
        image_name="AHD_6008.jpg",
        image_path="data/images/AHD_6008.jpg",
        description="Wedding",
        mood="Happy",
        quality_score=9.4,
        importance_score=9.8
    )

    assert image.quality_score > 0
    assert image.importance_score > 0