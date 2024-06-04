from openai import OpenAI

key = "sk-proj-B7WyHw3I6icB1xQQOFo0T3BlbkFJtOhXU9WjkHHXasOnkh6h"

def mainAI():
    client = OpenAI(api_key = key)

    response = client.images.generate(
        model = "dall-e-3",
        prompt = "A cute baby seal",
        size = "1024x1024",
        quality = "standard",
        n = 1,
    )

    image_url = response.data[0].url

    print(image_url)











# Old OpenAI (DOESN"T WORK!)
# openai.Image.create(
#     prompt = "A cute baby seal",
#     n = 2,
#     size = "1024x1024"
# )