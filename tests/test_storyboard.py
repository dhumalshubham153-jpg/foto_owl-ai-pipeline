from models.storyboard import Scene


def test_scene():

    from models.storyboard import Scene

def test_scene():

    scene = Scene(
        scene_number=1,
        image_name="AHD_6008.jpg",
        image_path="data/images/AHD_6008.jpg",
        duration=5,
        caption="Bride smiling",
        transition="Smooth"
    )

    assert scene.image_name == "AHD_6008.jpg"

    assert scene.duration == 5