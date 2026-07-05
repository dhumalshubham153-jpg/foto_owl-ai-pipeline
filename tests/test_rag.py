from services.chroma_service import ChromaService

rag = ChromaService()

rag.load_documents()

print("=" * 50)

print(rag.search_style("cinematic wedding"))

print("=" * 50)

print(rag.search_remotion("sequence component"))