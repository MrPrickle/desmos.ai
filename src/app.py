import sys
import os



current_dir = os.path.dirname(os.path.abspath(__file__))

scripts_dir = os.path.join(current_dir, 'src')

sys.path.insert(0, scripts_dir)

# sys.path.insert(0, 'C:/Users/Riche/OneDrive/Desktop/Documents/.github/desmos.ai/src/decor.py')  # Add the script's directory to the Python path
# sys.path.insert(1, 'C:/Users/Riche/OneDrive/Desktop/Documents/.github/desmos.ai/src/main.py')  # Add the script's directory to the Python path

import decor
import main

# Decoration
decor.mainUI()


# Text to Image


# Image to Black and White


# Image outline


# To desmos

