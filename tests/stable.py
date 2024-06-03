from diffusers import DiffusionPipeline

from diffusers import StableDiffusionPipeline, EulerDiscreteScheduler

from PIL import Image

import torch

model_id = "stabilityai/stable-diffusion-xl-base-1.0"
scheduler = EulerDiscreteScheduler.from_pretrained(model_id, subfolder="scheduler")
pipe = StableDiffusionPipeline.from_pretrained(model_id, scheduler=scheduler, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

prompt = "a photo of an astronaut riding a horse on mars"
image = pipe(prompt).images[0]

image.save("generated_image.png")