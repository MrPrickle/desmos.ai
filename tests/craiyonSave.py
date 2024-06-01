from craiyon import Craiyon, craiyon_utils
from PIL import Image  # Ensure you have pillow installed: pip install pillow
from io import BytesIO
import base64

# Initialize the Craiyon API wrapper
generator = Craiyon()

# Generate images with the prompt
result = generator.generate("Professional photo of Obama flashing a flag with his last name")
print(result.description)  # This should print the description of the generated images

# Encode the images in base64
images = craiyon_utils.encode_base64(result.images)

# Loop through the images and save each one as a .png file
for idx, img_data in enumerate(images):
    # Decode the base64 image
    image = Image.open(BytesIO(base64.decodebytes(img_data)))

    # Convert and save the image
    image_filename = f'generated_image_{idx + 1}.png'
    image.convert("RGBA").save(image_filename, "PNG")
    print(f"Saved {image_filename}")