# src/main.py
import argparse
from .model import DiffusionModel
from .preprocess import TextPreprocessor
from .inference import InferenceEngine

def main():
    parser = argparse.ArgumentParser(description="Text-to-Image Generation Pipeline")
    parser.add_argument("--prompt", type=str, required=True, help="Text prompt for image generation")
    parser.add_argument("--output", type=str, default="output.png", help="Output image path")
    args = parser.parse_args()

    preprocessor = TextPreprocessor()
    model = DiffusionModel(model_path="path/to/model", use_onnx=True)
    engine = InferenceEngine(model, preprocessor)
    engine.generate_image(args.prompt, args.output)

if __name__ == "__main__":
    main()