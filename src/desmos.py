from PIL import Image
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

frame = multiprocessing.Value('i', 0)
height = multiprocessing.Value('i', 0, lock = False)
width = multiprocessing.Value('i', 0, lock = False)
# frame_latex = 0 #


def get_contours(filename, nudge = .33):
    image = cv2.imread(filename)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if BILATERAL_FILTER:
        median = max(10, min(245, np.median(gray)))
        lower = int(max(0, (1 - nudge) * median))
        upper = int(min(255, (1 + nudge) * median))
        filtered = cv2.bilateralFilter(gray, 5, 50, 50)
        edged = cv2.Canny(filtered, lower, upper, L2gradient = USE_L2_GRADIENT)
    else:
        edged = cv2.Canny(gray, 30, 200)

    # REMOVED MULTIPROCESSING PART#
    # with frame.get_lock():
    #     frame.value += 1
    #     height.value = max(height.value, image.shape[0])
    #     width.value = max(width.value, image.shape[1])
    # print('\r--> Frame %d/%d' % (frame.value, len(os.listdir(FRAME_DIR))), end='')

    return edged[::-1]


def get_trace(data):
    for i in range(len(data)):
        data[i][data[i] > 1] = 1
    bmp = potrace.Bitmap(data)
    path = bmp.trace(2, potrace.TURNPOLICY_MINORITY, 1.0, 1, .5)
    return path


def get_latex(filename):
    latex = []
    path = get_trace(get_contours(filename))

    for curve in path.curves:
        segments = curve.segments
        start = curve.start_point
        for segment in segments:
            x0, y0 = start
            if segment.is_corner:
                x1, y1 = segment.c
                x2, y2 = segment.end_point
                latex.append('((1-t)%f+t%f,(1-t)%f+t%f)' % (x0, x1, y0, y1))
                latex.append('((1-t)%f+t%f,(1-t)%f+t%f)' % (x1, x2, y1, y2))
            else:
                x1, y1 = segment.c1
                x2, y2 = segment.c2
                x3, y3 = segment.end_point
                latex.append('((1-t)((1-t)((1-t)%f+t%f)+t((1-t)%f+t%f))+t((1-t)((1-t)%f+t%f)+t((1-t)%f+t%f)),\
                (1-t)((1-t)((1-t)%f+t%f)+t((1-t)%f+t%f))+t((1-t)((1-t)%f+t%f)+t((1-t)%f+t%f)))' % \
                (x0, x1, x1, x2, x1, x2, x2, x3, y0, y1, y1, y2, y1, y2, y2, y3))
            start = segment.end_point
    return latex


def get_expressions(filename):
    exprid = 0
    exprs = []
    for expr in get_latex(filename):
        exprid += 1
        exprs.append({'id': 'expr-' + str(exprid), 'latex': expr, 'color': COLOUR, 'secret': True})
    return exprs


# REMOVED MULTIPROCESSING FUNCTION
# def get_expressions(frame):
#     exprid = 0
#     exprs = []
#     for expr in get_latex(FRAME_DIR + '/frame%d.%s' % (frame+1, FILE_EXT)):
#         exprid += 1
#         exprs.append({'id': 'expr-' + str(exprid), 'latex': expr, 'color': COLOUR, 'secret': True})
#     return exprs
