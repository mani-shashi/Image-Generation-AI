# src/api.py
from fastapi import FastAPI
from pydantic import BaseModel
from .inference import InferenceEngine

app = FastAPI()

class TextPrompt(BaseModel):
    prompt: str
    output_path: str

@app.post("/generate")
async def generate_image(prompt: TextPrompt):
    engine = InferenceEngine(...)  # Initialize with model and preprocessor
    image = engine.generate_image(prompt.prompt, prompt.output_path)
    return {"status": "success", "output_path": prompt.output_path}