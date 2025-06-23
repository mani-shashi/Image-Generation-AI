import os

MODEL_PATH = "path/to/stable_diffusion_model"
ONNX_MODEL_PATH = "path/to/onnx_model"
TENSORRT_MODEL_PATH = "path/to/tensorrt_model"
BATCH_SIZE = 1
PRECISION = "fp16"  

CUDA_AVAILABLE = os.getenv("CUDA_AVAILABLE", "true").lower() == "true"
OUTPUT_DIR = "outputs/"