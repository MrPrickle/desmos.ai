import sys
import os
import requests
import cv2
import numpy as np

# Add the 'src' directory to the Python path

current_dir = os.path.dirname(os.path.abspath(__file__))
print(f"Current directory: {current_dir}")

scripts_dir = os.path.join(current_dir, 'src')
print(f"Scripts directory: {scripts_dir}")

sys.path.insert(0, scripts_dir)

# Import the necessary modules
import structure
import main
from desmos_test import get_expressions  # Explicitly import the function

# Text to Image -------------------------------------------

realUserPrompt = ""

def getPrompt(prompt):
    realUserPrompt = prompt

# Call main.py function to get the image URL
def startUp():
    image_url = structure.generate_image_url(realUserPrompt)
    print(f"Generated image URL: {image_url}")

    # Download the image from the URL
    response = requests.get(image_url)
    image_data = np.asarray(bytearray(response.content), dtype="uint8")
    image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)

    # Ensure the 'images' directory exists
    images_dir = os.path.join(current_dir, 'images')
    print(f"Images directory: {images_dir}")

    os.makedirs(images_dir, exist_ok=True)
    print("Images directory created or already exists.")

    # Save the image to the 'images' directory
    image_filename = 'temp_image.png'
    temp_image_path = os.path.join(images_dir, image_filename)
    print(f"Temporary image path: {temp_image_path}")

    cv2.imwrite(temp_image_path, image)
    print("Image saved successfully.")

    # Call get_expressions with the local image path
    expressions = get_expressions(temp_image_path)
    print("Expressions obtained from image")

    def write_to_txt(expressions, filename):
        with open(filename, 'w') as file:
            for expr in expressions:
                file.write(expr + '\n')

    def get_final_latex(filename, output_file):
        latex = get_expressions(filename)
        write_to_txt(latex, output_file)

    test_img_path = temp_image_path  # Use the temporary image path directly
    print(f"Test image path: {test_img_path}")

    get_final_latex(test_img_path, "latex.txt")
    print("Latex file created successfully.")

    # Clean up the temporary image file
    os.remove(temp_image_path)
    print("Temporary image file removed.")

# Call the mainUI function from the decor module ----------



# Image to Black and White --------------------------------


# Image outline -------------------------------------------


# To Desmos -----------------------------------------------


# Send Equations