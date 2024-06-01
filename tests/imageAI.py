from craiyon import Craiyon, craiyon_utils # Importing the v3 model
from PIL import Image # pip install pillow
from io import BytesIO
import base64

apiToken = "eyJhbGciOiJIUzI1NiIsImtpZCI6ImdIYUZTeTdZVVprckQxdWMiLCJ0eXAiOiJKV1QifQ.eyJhdWQiOiJhdXRoZW50aWNhdGVkIiwiZXhwIjoxNzE3Nzk3MTkzLCJpYXQiOjE3MTcxOTIzOTMsImlzcyI6Imh0dHBzOi8vYnl6enllbmdweHR5c3NkanBnd3Iuc3VwYWJhc2UuY28vYXV0aC92MSIsInN1YiI6ImZlYTMwZGVlLWU3M2EtNDM5Ni1iN2Q5LTYyMmFmYmQxYjE5MiIsImVtYWlsIjoicmF5Zm9yZC5saUBnbWFpbC5jb20iLCJwaG9uZSI6IiIsImFwcF9tZXRhZGF0YSI6eyJwcm92aWRlciI6Imdvb2dsZSIsInByb3ZpZGVycyI6WyJnb29nbGUiXX0sInVzZXJfbWV0YWRhdGEiOnsiYXZhdGFyX3VybCI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FDZzhvY0pHYkNWOTM1bjhJeVNqVTNXVGVySUNkcDU2eGtaTXFIbnpKcGZiQ3Nac3RuZzdHUXRmPXM5Ni1jIiwiZW1haWwiOiJyYXlmb3JkLmxpQGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJmdWxsX25hbWUiOiJXaWxsaWFtIExpIiwiaXNzIjoiaHR0cHM6Ly9hY2NvdW50cy5nb29nbGUuY29tIiwibmFtZSI6IldpbGxpYW0gTGkiLCJwaG9uZV92ZXJpZmllZCI6ZmFsc2UsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQ2c4b2NKR2JDVjkzNW44SXlTalUzV1RlcklDZHA1NnhrWk1xSG56SnBmYkNzWnN0bmc3R1F0Zj1zOTYtYyIsInByb3ZpZGVyX2lkIjoiMTAxNDQ5NzM3NDQ2ODUwMDMwNDI4Iiwic3ViIjoiMTAxNDQ5NzM3NDQ2ODUwMDMwNDI4In0sInJvbGUiOiJhdXRoZW50aWNhdGVkIiwiYWFsIjoiYWFsMSIsImFtciI6W3sibWV0aG9kIjoib2F1dGgiLCJ0aW1lc3RhbXAiOjE3MTcxOTIzOTN9XSwic2Vzc2lvbl9pZCI6IjUxNDdlOGQzLWI5NmMtNGY2Yy1hNjEyLTUwZjQwOWM5Yzk5NiIsImlzX2Fub255bW91cyI6ZmFsc2V9.Xl_bCil5J3fGSLF8i8gOE3I-oFnc7h3d31E4I8p-7eM"

def mainAI():

    # api_token and model_version are not required, but recommended
    # generator = Craiyon(api_token=apiToken, model_version="c4ue22fb7kb6wlac")

    generator = Craiyon(model_version="vs")

    # ...rest is the same stuff as above
    # generator = Craiyon() # Instantiates the api wrapper without an API_token
    result = generator.generate("Professional photo of Obama flashing a flag with his last name") # Generates 9 images by default and you cannot change that
    print(result.description) # >>> Obama holding up a flag with his last name, smiling confidently

    # Encode the images in base64
    images = craiyon_utils.encode_base64(result.images)
    
    # Store image objects in a list
    image_objects = []

    # Loop through the images and convert to PIL Image objects
    for img_data in enumerate(images):
        # Decode the base64 image
        image = Image.open(BytesIO(base64.decodebytes(img_data)))
        image_objects.append(image)
    # To convert the .webp images to .jpg or .png, you can proceed like this
    # image.convert("RGB").save("image.jpg", "JPEG") # For ".jpg" images
    # image.convert("RGBA").save("image.png", "PNG") # For ".png" images
    
    # Use the PIL's Image object as per your needs

    return image_objects


if __name__ == "__main__":
    mainAI()