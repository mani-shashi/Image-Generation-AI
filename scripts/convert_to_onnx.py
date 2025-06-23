import torch
from diffusers import StableDiffusionPipeline

# Load the pre-trained Stable Diffusion model
model_id = "runwayml/stable-diffusion-v1-5"
pipeline = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)

# Define a dummy input for tracing
dummy_prompt = "a photo of an astronaut riding a horse on mars"
dummy_negative_prompt = ""
dummy_height = 512
dummy_width = 512
dummy_guidance_scale = 7.5
dummy_num_inference_steps = 50

# Export the text encoder
text_encoder_path = "text_encoder.onnx"
print(f"Exporting text encoder to {text_encoder_path}...")
torch.onnx.export(
    pipeline.text_encoder,
    (pipeline.tokenizer(dummy_prompt, padding="max_length", max_length=pipeline.tokenizer.model_max_length, truncation=True, return_tensors="pt").input_ids),
    text_encoder_path,
    input_names=["input_ids"],
    output_names=["last_hidden_state"],
    dynamic_axes={"input_ids": {0: "batch_size"}, "last_hidden_state": {0: "batch_size"}},
    opset_version=14,
)
print("Text encoder exported.")

# Export the UNet model
unet_path = "unet.onnx"
print(f"Exporting UNet to {unet_path}...")
dummy_sample = torch.randn(1, 4, dummy_height // 8, dummy_width // 8)
dummy_timestep = torch.tensor(999)
dummy_encoder_hidden_states = torch.randn(1, 77, 768)
torch.onnx.export(
    pipeline.unet,
    (dummy_sample, dummy_timestep, dummy_encoder_hidden_states),
    unet_path,
    input_names=["sample", "timestep", "encoder_hidden_states"],
    output_names=["out_sample"],
    dynamic_axes={
        "sample": {0: "batch_size", 
                   2: "height",
                   3: "width"},
        "timestep": {0: "batch_size"},
        "encoder_hidden_states": {0: "batch_size", 1: "sequence_length"},
    },
    opset_version=14,
)
print("UNet exported.")

# Export the VAE decoder
vae_decoder_path = "vae_decoder.onnx"
print(f"Exporting VAE decoder to {vae_decoder_path}...")
dummy_latent_sample = torch.randn(1, 4, dummy_height // 8, dummy_width // 8)
torch.onnx.export(
    pipeline.vae.decode,
    dummy_latent_sample,
    vae_decoder_path,
    input_names=["latent_sample"],
    output_names=["sample"],
    dynamic_axes={
        "latent_sample": {0: "batch_size", 
                          2: "height",
                          3: "width"},
    },
    opset_version=14,
)
print("VAE decoder exported.")

print("All models exported to ONNX successfully!")