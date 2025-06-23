# src/utils.py
import logging
import time
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def save_image(image, output_path: str):
    """Save generated image to disk."""
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    image.save(output_path)
    logger.info(f"Image saved to {output_path}")

def measure_inference_time(func):
    """Decorator to measure inference time."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        logger.info(f"Inference time: {time.time() - start_time:.2f} seconds")
        return result
    return wrapper