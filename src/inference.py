# src/inference.py
import torch
from PIL import Image
import numpy as np

class InferenceEngine:
    def __init__(self, model, preprocessor):
        self.model = model
        self.preprocessor = preprocessor

    def generate_image(self, prompt: str, output_path: str):
        """Generate image from text prompt."""
        input_ids, attention_mask = self.preprocessor.preprocess_text(prompt)
        if self.model.use_onnx:
            # ONNX/TensorRT inference
            outputs = self.model.session.run(None, {
                "input_ids": input_ids.numpy(),
                "attention_mask": attention_mask.numpy()
            })
            image = outputs[0]
        else:
            image = self.model.pipeline(prompt).images[0]
        image.save(output_path)
        return image