import os
import torch
from PIL import Image
from diffusers import DiffusionPipeline

# Load the pre-trained model
# You can replace 'runwayml/stable-diffusion-v1-5' with other models if needed
pipeline = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
pipeline.to("cuda")

def generate_image(prompt: str, output_dir: str = "generated_images", filename: str = "output.png"):
    """
    Generates an image based on the given prompt using the loaded diffusion pipeline.

    Args:
        prompt (str): The text prompt to guide image generation.
        output_dir (str): The directory where the generated image will be saved.
        filename (str): The name of the output image file.
    """
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, filename)

    print(f"Generating image for prompt: '{prompt}'...")
    with torch.no_grad():
        image = pipeline(prompt).images[0]

    image.save(output_path)
    print(f"Image saved to {output_path}")

if __name__ == "__main__":
    # Example usage:
    test_prompt = "A futuristic city at sunset, highly detailed, cyberpunk style"
    generate_image(test_prompt)

    test_prompt_2 = "A serene landscape with a flowing river and mountains, oil painting"
    generate_image(test_prompt_2, filename="serene_landscape.png", output_dir="my_images")
