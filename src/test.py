import torch
from diffusers import DiffusionPipeline, StableDiffusionPipeline, EulerDiscreteScheduler
from PIL import Image

# Check if PyTorch is available
print("Torch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())

# Basic operation with diffusers
model_id = "stabilityai/stable-diffusion-2"
try:
    scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
    pipe = StableDiffusionPipeline.from_pretrained(model_id, scheduler=scheduler, torch_dtype=torch.float16)
    print("Diffusers library is working correctly.")
except Exception as e:
    print("Error with diffusers library:", e)

# Basic operation with Pillow
try:
    img = Image.new('RGB', (60, 30), color = (73, 109, 137))
    img.save('pil_test_image.png')
    print("Pillow library is working correctly.")
except Exception as e:
    print("Error with Pillow library:", e)
