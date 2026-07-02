from app.services.extractor import AudioExtractor

extractor = AudioExtractor()

result = extractor.extract_audio(
    "uploads/02d6f022e137462aba2575e762a5aa02.mp4"
)

print(result)