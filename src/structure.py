from openai import OpenAI

key = "sk-proj-B7WyHw3I6icB1xQQOFo0T3BlbkFJtOhXU9WjkHHXasOnkh6h"

def generate_image_url(prompt):
    client = OpenAI(api_key=key)

    response = client.images.generate(
        model="dall-e-3",
        prompt="prompt",
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url

    print(image_url)

    return image_url













# Old OpenAI (DOESN"T WORK!)
# openai.Image.create(
#     prompt = "A cute baby seal",
#     n = 2,
#     size = "1024x1024"
# )