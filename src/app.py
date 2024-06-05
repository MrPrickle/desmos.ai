import sys
import os



current_dir = os.path.dirname(os.path.abspath(__file__))

scripts_dir = os.path.join(current_dir, 'src')

sys.path.insert(0, scripts_dir)

# sys.path.insert(0, 'C:/Users/Riche/OneDrive/Desktop/Documents/.github/desmos.ai/src/decor.py')  # Add the script's directory to the Python path
# sys.path.insert(1, 'C:/Users/Riche/OneDrive/Desktop/Documents/.github/desmos.ai/src/main.py')  # Add the script's directory to the Python path

from src import decor
from src import main
from src import desmos


# Text to Image -------------------------------------------

# Call main.py function to get the image URL
image_url = main.generate_image_url()

# Call get_expressions with the image URL
expressions = desmos.get_expressions(image_url)

# Call the mainUI function from the decor module ----------
decor.mainUI()


# Image to Black and White --------------------------------


# Image outline -------------------------------------------


# To Desmos -----------------------------------------------


# Send Equations