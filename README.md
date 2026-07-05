#  FotoOwl AI Pipeline

An AI-powered multi-agent video generation pipeline built using LangGraph, Gemini, ChromaDB and Remotion.

---

# Features

- Multi-Agent LangGraph Pipeline
- Gemini Vision Image Analysis
- Gemini Intent Parsing
- Storyboard Generation
- ChromaDB RAG
- Remotion Script Generation
- Compiler & Retry Loop
- Renderer
- JSON Output Generation

---

# Architecture

User Prompt
        │
        ▼
Intent Parser
        │
        ▼
Image Analyzer
        │
        ▼
Storyboard Writer
        │
        ├──────────────► ChromaDB
        │
        ▼
Script Generator
        │
        ├──────────────► ChromaDB
        ▼
Compiler
        │
Retry ◄──┘
        │
        ▼
Renderer
        │
        ▼
Output

---

# Folder Structure

```
fotoowl-ai-pipeline/

agents/
graph/
models/
services/
rag/
tests/
output/
data/

main.py
README.md
requirements.txt
```

---

# Tech Stack

- Python
- LangGraph
- Gemini 2.5 Flash
- ChromaDB
- Sentence Transformers
- Pydantic
- Pillow
- Remotion
- TypeScript

---

# AI Agents

## 1. Intent Parser

Converts natural language prompts into structured video intent.

---

## 2. Image Analyzer

Uses Gemini Vision to analyze every uploaded image.

---

## 3. Storyboard Writer

Creates a storyboard using image analysis and retrieved style guides.

---

## 4. Script Generator

Generates a Remotion TSX composition using RAG.

---

## 5. Compiler & Fixer

Checks generated scripts and retries if compilation fails.

---

## 6. Renderer

Produces the final video output.

---

# RAG

Two ChromaDB collections are used.

Style Guides

- Cinematic
- Upbeat
- Corporate

Remotion Documentation

- Img
- Sequence
- Transitions

---

# Output Files

output/

- remotion.tsx
- storyboard.json
- pipeline_state.json
- final_video.mp4

---

# Future Improvements

- Real Remotion rendering
- Automatic image ranking
- Video caption generation
- Music recommendation
- Multi-language support

---

# Author

Shubham Dhumal