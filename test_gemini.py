from services.gemini_service import analyze_single_image

result = analyze_single_image("data/test.jpg")

print(result)
print(result.description)
print(result.quality_score)