import torch
import time
from diffusers import DiffusionPipeline

def run_benchmark(model_id, num_inference_steps=50, num_runs=5):
    """
    Runs a benchmark for a given diffusion model.

    Args:
        model_id (str): The ID of the pre-trained model from Hugging Face.
        num_inference_steps (int): The number of inference steps to use.
        num_runs (int): The number of times to run the inference for averaging.

    Returns:
        dict: A dictionary containing benchmark results (average time, std dev).
    """
    print(f"Loading model: {model_id}...")
    pipeline = DiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
    pipeline.to("cuda")
    print("Model loaded.")

    prompt = "a photo of an astronaut riding a horse on mars"
    times = []

    print(f"Starting benchmark for {model_id} with {num_inference_steps} inference steps over {num_runs} runs...")
    for i in range(num_runs):
        start_time = time.time()
        _ = pipeline(prompt, num_inference_steps=num_inference_steps).images[0]
        end_time = time.time()
        times.append(end_time - start_time)
        print(f"Run {i+1}/{num_runs}: {times[-1]:.2f} seconds")

    avg_time = sum(times) / num_runs
    std_dev = (sum([(x - avg_time) ** 2 for x in times]) / num_runs) ** 0.5

    results = {
        "model_id": model_id,
        "num_inference_steps": num_inference_steps,
        "num_runs": num_runs,
        "average_time_sec": avg_time,
        "std_dev_sec": std_dev,
        "all_times_sec": times
    }
    return results

if __name__ == "__main__":
    # Example usage:
    models_to_benchmark = [
        "runwayml/stable-diffusion-v1-5"
    ]