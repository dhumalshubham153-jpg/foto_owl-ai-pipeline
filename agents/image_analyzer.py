from services.gemini_service import analyze_image_batch
from models.state import PipelineState


BATCH_SIZE = 10


def image_analyzer(state: PipelineState) -> PipelineState:
    print("=" * 60)
    print("🖼️ Image Analyzer Agent Started")
    print("=" * 60)

    state.image_analysis.clear()

    if not state.image_paths:
        print("❌ No images found.")
        state.status = "no_images"
        return state

    total_images = len(state.image_paths)

    print(f"\n📂 Total Images : {total_images}")
    print(f"📦 Batch Size   : {BATCH_SIZE}")
    print(f"🚀 API Calls    : {(total_images + BATCH_SIZE - 1) // BATCH_SIZE}\n")

    # ---------------------------------------
    # Batch Processing
    # ---------------------------------------

    for start in range(0, total_images, BATCH_SIZE):

        batch = state.image_paths[start:start + BATCH_SIZE]

        batch_number = start // BATCH_SIZE + 1

        print("=" * 60)
        print(f"📦 Processing Batch {batch_number}")
        print(f"Images : {len(batch)}")
        print("=" * 60)

        try:

            analyses = analyze_image_batch(batch)

            for analysis in analyses:

                state.image_analysis.append(analysis)

                print(f"✔ {analysis.image_name}")
                print(f"Description : {analysis.description}")
                print(f"Mood        : {analysis.mood}")
                print(f"Quality     : {analysis.quality_score}")
                print(f"Importance  : {analysis.importance_score}")
                print("-" * 60)

        except Exception as e:

            print(f"❌ Batch {batch_number} Failed")
            print(e)

    # ---------------------------------------
    # Select Best Images
    # ---------------------------------------

    sorted_images = sorted(
        state.image_analysis,
        key=lambda image: image.importance_score,
        reverse=True
    )

    state.selected_images = [
        image.image_name
        for image in sorted_images[:5]
    ]

    print("\n" + "=" * 60)
    print("⭐ Top Selected Images")
    print("=" * 60)

    for i, image in enumerate(sorted_images[:5], start=1):
        print(
            f"{i}. {image.image_name} "
            f"(Importance: {image.importance_score})"
        )

    print("\n")
    print(f"✅ Total Images Analyzed : {len(state.image_analysis)}")
    print(f"🏆 Images Selected       : {len(state.selected_images)}")

    state.status = "images_analyzed"

    return state