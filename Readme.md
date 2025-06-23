
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

2.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Install Node.js Backend dependencies:**
    ```bash
    cd backend
    npm install
    ```

4.  **Install React Front-End dependencies:**
    ```bash
    cd frontend
    npm install
    ```

5.  **Run the Python FastAPI Backend:**
    ```bash
    uvicorn src.api:app --host 0.0.0.0 --port 8000
    ```

6.  **Run the Node.js Server:**
    ```bash
    cd backend
    npm start
    ```

7.  **Run the React Front-End:**
    ```bash
    cd frontend
    npm start
    ```

8.  **Open http://localhost:3000 in your browser**
   
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

