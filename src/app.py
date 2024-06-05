import sys
import os
import requests
import cv2
import numpy as np

# Add the 'src' directory to the Python path

current_dir = os.path.dirname(os.path.abspath(__file__))

scripts_dir = os.path.join(current_dir, 'src')

sys.path.insert(0, scripts_dir)

# Import the necessary modules
import main
import decor
from desmos import get_expressions  # Explicitly import the function

# Text to Image -------------------------------------------

# Call main.py function to get the image URL
image_url = main.generate_image_url()

# Download the image from the URL
response = requests.get(image_url)
image_data = np.asarray(bytearray(response.content), dtype="uint8")
image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)

# Ensure the 'images' directory exists
images_dir = os.path.join(current_dir, 'images')
os.makedirs(images_dir, exist_ok=True)

# Save the image to the 'images' directory
image_filename = 'temp_image.png'
temp_image_path = os.path.join(images_dir, image_filename)
cv2.imwrite(temp_image_path, image)

# Call get_expressions with the local image path
expressions = get_expressions(temp_image_path)
print("")
print("")

print(expressions)

# Clean up the temporary image file
os.remove(temp_image_path)

# Call the mainUI function from the decor module ----------
decor.mainUI()



# Image to Black and White --------------------------------


# Image outline -------------------------------------------


# To Desmos -----------------------------------------------


# Send Equations