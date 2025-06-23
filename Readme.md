
## Introduction

This project aims to explore and implement different techniques for AI-driven image generation. We leverage deep learning models to create novel images, offering insights into the capabilities of generative adversarial networks (GANs) and variational autoencoders (VAEs).

## Features

- **Text-to-Image Generation:** Generate images from textual descriptions.
- **Image-to-Image Translation:** Transform images from one domain to another (e.g., day to night, sketches to photos).
- **Style Transfer:** Apply the artistic style of one image to the content of another.
- **High-Resolution Output:** Support for generating high-resolution images.
- **Customizable Models:** Easily modify and experiment with different model architectures and parameters.

## Installation

To get started with this project, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/mani-shashi/image-generation-ai.git
    cd image-generation-ai
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Generating Images

To generate images, you can use the provided scripts.

**Text-to-Image:**
```bash
python generate_text_to_image.py --prompt "a futuristic city at sunset" --output_path output/city_sunset.png
```

**Image-to-Image Translation:**
```bash
python generate_image_to_image.py --input_image input/sketch.png --model_type edges2photos --output_path output/photo_from_sketch.png
```

