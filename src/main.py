import requests
import json

url = "https://modelslab.com/api/v6/images/text2img"

payload = json.dumps({
	"key": "",
    "model_id": "ae-sdxl-v1",
    "prompt": "ultra realistic close up portrait ((A smart and handsome man named leo)), brown eyes, shaved side haircut, hyper detail, cinematic lighting, magic neon, dark red city, Canon EOS R3, nikon, f/1.4, ISO 200, 1/160s, 8K, RAW, unedited, symmetrical balance, in-frame, 8K",
    "negative_prompt": "painting, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, deformed, ugly, blurry, bad anatomy, bad proportions, extra limbs, cloned face, skinny, glitchy, double torso, extra arms, extra hands, mangled fingers, missing lips, ugly face, distorted face, extra legs, anime",
    "width": "512",
    "height": "512",
    "samples": "1",
    "num_inference_steps": "30",
    "safety_checker": "no",
    "enhance_prompt": "yes",
    "seed": 56,
    "guidance_scale": 7.5,
    "multi_lingual": "no",
    "panorama": "no",
    "self_attention": "no",
    "upscale": "no",
    "embeddings_model": None,
    "lora_model": None,
    "tomesd": "yes",
    "use_karras_sigmas": "yes",
    "vae": None,
    "lora_strength": None,
    "scheduler": "UniPCMultistepScheduler",
    "webhook": None,
    "track_id": None
})

headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

response_data = response.json

print(response.text)

print(json.dumps(response_data, indent=4))