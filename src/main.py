import requests
import json

url = "https://modelslab.com/api/v6/images/text2img"

payload = json.dumps({
    "key": "api-key",
    "model_id": "ae-sdxl-v1",
    "prompt": "ultra realistic close up portrait ((beautiful pale female with heavy black eyeliner and big boob and big ass thicc thighs)), blue eyes, shaved side haircut, hyper detail, cinematic lighting, magic neon, dark red city, Canon EOS R3, nikon, f/1.4, ISO 200, 1/160s, 8K, RAW, unedited, symmetrical balance, in-frame, 8K",
    "negative_prompt": "painting, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, deformed, ugly, blurry, bad anatomy, bad proportions, extra limbs, cloned face, skinny, glitchy, double torso, extra arms, extra hands, mangled fingers, missing lips, ugly face, distorted face, extra legs, anime",
    "width": "512",
    "height": "512",
    "samples": "1",
    "num_inference_steps": "30",
    "seed": null,
    "guidance_scale": 7.5,
    "scheduler": "UniPCMultistepScheduler",
    "webhook": null,
    "track_id": null
})

headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)