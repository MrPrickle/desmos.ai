from PIL import Image
import os
import numpy as np
import potrace
import cv2

# UNUSED MULTIPROCESSING LIBRARIES
# import multiprocessing
# from time import time
# import os
# import sys
# import getopt
# import traceback
# import webbrowser
# from threading import Timer

# REAL GLOBAL VARIABLES
COLOUR = '#2464b4' # Hex value of colour for graph output	
BILATERAL_FILTER = False # Reduce number of lines with bilateral filter
USE_L2_GRADIENT = False # Creates less edges but is still accurate (leads to faster renders)

# OLD GLOBAL VARIABLES
# FRAME_DIR = 'frames' # The folder where the frames are stored relative to this file
# FILE_EXT = 'png' # Extension for frame files
# COLOUR = '#2464b4' # Hex value of colour for graph output	
# SCREENSHOT_SIZE = [ None, None ] # [width, height] for downloaded images
# SCREENSHOT_FORMAT = 'png' # Format to use when downloading images
# OPEN_BROWSER = True # Open default browser automatically #

# BILATERAL_FILTER = False # Reduce number of lines with bilateral filter
# DOWNLOAD_IMAGES = False # Download each rendered frame automatically (works best in firefox) #
# USE_L2_GRADIENT = False # Creates less edges but is still accurate (leads to faster renders)
# SHOW_GRID = True # Show the grid in the background while rendering #

# frame = multiprocessing.Value('i', 0)
# height = multiprocessing.Value('i', 0, lock = False)
# width = multiprocessing.Value('i', 0, lock = False)
# frame_latex = 0 #


# def get_contours(filename, nudge=.33):
#     image = cv2.imread(filename)

#     if image is None:
#         raise ValueError(f"Image at {filename} could not be read")

#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Apply Gaussian blur to the grayscale image
#     blurred = cv2.GaussianBlur(gray, (5, 5), 0)

#     # Perform Canny edge detection
#     edged = cv2.Canny(blurred, 30, 200)

#     # Find contours in the edge-detected image
#     contours, _ = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

#     return contours


def get_contours(filename, nudge=.33):
    image = cv2.imread(filename)

    if image is None:
        raise ValueError(f"Image at {filename} could not be read")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to enhance contour detection
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Perform Canny edge detection
    edged = cv2.Canny(blurred, 30, 200)

    # Find contours in the edge-detected image
    contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    return contours


# def get_contours(filename, nudge=.33):
#     image = cv2.imread(filename)

#     if image is None:
#         raise ValueError(f"Image at {filename} could not be read")

#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     if BILATERAL_FILTER:
#         median = max(10, min(245, np.median(gray)))
#         lower = int(max(0, (1 - nudge) * median))
#         upper = int(min(255, (1 + nudge) * median))
#         filtered = cv2.bilateralFilter(gray, 5, 50, 50)
#         edged = cv2.Canny(filtered, lower, upper, L2gradient=USE_L2_GRADIENT)
#     else:
#         edged = cv2.Canny(gray, 30, 200)

# #     contours, _ = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# #     return contours

    # REMOVED MULTIPROCESSING PART#
    # with frame.get_lock():
    #     frame.value += 1
    #     height.value = max(height.value, image.shape[0])
    #     width.value = max(width.value, image.shape[1])
    # print('\r--> Frame %d/%d' % (frame.value, len(os.listdir(FRAME_DIR))), end='')


def get_trace(data):
    # Convert the contour data into a binary image
    binary_image = np.zeros((500, 500), dtype=np.uint8)
    cv2.drawContours(binary_image, data, -1, (255), 1)

    # Invert the binary image
    binary_image = cv2.bitwise_not(binary_image)

    # Ensure that the image is binary
    binary_image[binary_image != 0] = 255

    # Create a Bitmap object from the binary image
    bmp = potrace.Bitmap(binary_image)

    # Trace the bitmap
    path = bmp.trace(2, potrace.POTRACE_TURNPOLICY_MINORITY, 1.0, 1, .5)
    return path



def get_latex(filename):
    latex = []
    path = get_trace(get_contours(filename))
    height = 500  # Assuming image height is 500, adjust if necessary

    for curve in path:
        segments = curve.segments
        start = (curve.start_point.x, height - curve.start_point.y)  # Flip y-coordinate
        for segment in segments:
            if segment.is_corner:
                control = (segment.c.x, height - segment.c.y)  # Flip y-coordinate
                end = (segment.end_point.x, height - segment.end_point.y)  # Flip y-coordinate
                # Construct LaTeX expression for a straight line segment
                latex.append(f"((1-t)*({start[0]})+t*({control[0]}),(1-t)*({start[1]})+t*({control[1]}))")
                latex.append(f"((1-t)*({control[0]})+t*({end[0]}),(1-t)*({control[1]})+t*({end[1]}))")
            else:
                control1 = (segment.c1.x, height - segment.c1.y)  # Flip y-coordinate
                control2 = (segment.c2.x, height - segment.c2.y)  # Flip y-coordinate
                end = (segment.end_point.x, height - segment.end_point.y)  # Flip y-coordinate
                # Construct LaTeX expression for a Bezier curve segment
                latex.append(f"((1-t)*((1-t)*({start[0]})+t*({control1[0]}))+t*((1-t)*({control1[0]})+t*({control2[0]})),\
                            (1-t)*((1-t)*({start[1]})+t*({control1[1]}))+t*((1-t)*({control1[1]})+t*({control2[1]})))")
                latex.append(f"((1-t)*((1-t)*({control1[0]})+t*({control2[0]}))+t*((1-t)*({control2[0]})+t*({end[0]})),\
                            (1-t)*((1-t)*({control1[1]})+t*({control2[1]}))+t*((1-t)*({control2[1]})+t*({end[1]})))")
            start = end  # Update start point for the next segment
    return latex



# def get_expressions(filename):
#     exprid = 0
#     exprs = []
#     for expr in get_latex(filename):
#         exprid += 1
#         exprs.append({'latex': expr})
#     return exprs

def get_expressions(filename):
    latex = []
    for expr in get_latex(filename):
        latex.append(expr)
    return latex


def write_to_txt(expressions, filename):
    with open(filename, 'w') as file:
        for expr in expressions:
            file.write(expr + '\n')

def get_final_latex(filename, output_file):
    latex = get_expressions(filename)
    write_to_txt(latex, output_file)



# REMOVED MULTIPROCESSING FUNCTION
# def get_expressions(frame):
#     exprid = 0
#     exprs = []
#     for expr in get_latex(FRAME_DIR + '/frame%d.%s' % (frame+1, FILE_EXT)):
#         exprid += 1
#         exprs.append({'id': 'expr-' + str(exprid), 'latex': expr, 'color': COLOUR, 'secret': True})
#     return exprs


# Test:


# current_dir = os.path.dirname(os.path.abspath(__file__))
# temp_img_dir = os.path.join(current_dir, 'images')


test_img_path =  "C:\\Users\\Willi\\OneDrive\\Documents\\GitHub\\desmos.ai-1\\src\\images\\temp_image.png"

print(get_expressions(test_img_path))

get_final_latex(test_img_path, "latex.txt")
