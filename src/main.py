from openai import OpenAI
client = OpenAI()

response = ""

response = client.images.generate(
  model = "dall-e-3",
  prompt = "gyatt recoil",
  size = "1024x1024",
  quality = "standard",
  n = 1,
)

image_url = response.data[0].url