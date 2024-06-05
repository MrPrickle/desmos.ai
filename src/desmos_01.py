import cv2
import numpy as np
import potrace
from potrace import Bitmap, POTRACE_TURNPOLICY_MINORITY

COLOUR = '#2464b4'
BILATERAL_FILTER = False
USE_L2_GRADIENT = False

def get_contours(filename, nudge=.33):
    image = cv2.imread(filename)
    if image is None:
        raise ValueError(f"Image at {filename} could not be read")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 30, 200)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    print("Number of contours:", len(contours))  # Print number of detected contours

    # Display the original image with contours (optional)
    contour_image = image.copy()
    cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)
    cv2.imshow('Contours', contour_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return contours  # Return detected contours

def get_trace(contours):
    for contour in contours:
        # Create a binary image from the contour data
        height, width = 500, 500  # Set dimensions according to your image size
        contour_image = np.zeros((height, width), dtype=np.uint8)  # Initialize an empty image
        cv2.drawContours(contour_image, contour, -1, (255), 1)  # Draw contours on the image

        # Invert the image (if necessary)
        contour_image = cv2.bitwise_not(contour_image)

        # Ensure that the image is binary (convert to binary if necessary)
        contour_image[contour_image != 0] = 255

        print("Contour image shape:", contour_image.shape)  # Print shape of the contour image

        # Create a Bitmap object from the binary image
        bmp = potrace.Bitmap(contour_image)

        # Trace the bitmap
        path = bmp.trace(2, potrace.POTRACE_TURNPOLICY_MINORITY, 1.0, 1, .5)
        print("Number of paths:", len(path))  # Print number of traced paths

def get_latex(filename):
    latex = []
    contours = get_contours(filename)

    for contour in contours:
        bmp = Bitmap(contour)
        path = bmp.trace(2, POTRACE_TURNPOLICY_MINORITY, 1.0, 1, .5)
        for curve in path:
            segments = curve.segments
            latex_expr = ""  # Initialize LaTeX expression string
            start = (curve.start_point.x, curve.start_point.y)
            for segment in segments:
                if segment.is_corner:
                    control_point = (segment.c.x, segment.c.y)
                    end_point = (segment.end_point.x, segment.end_point.y)
                    # Append LaTeX expression for a straight line segment
                    latex_expr += f"((1-t){start}+t{control_point})"
                    latex_expr += f"--((1-t){control_point}+t{end_point})"
                else:
                    control_point1 = (segment.c1.x, segment.c1.y)
                    control_point2 = (segment.c2.x, segment.c2.y)
                    end_point = (segment.end_point.x, segment.end_point.y)
                    # Append LaTeX expression for a Bezier curve segment
                    latex_expr += f"((1-t)((1-t){start}+t{control_point1})+t((1-t){control_point1}+t{control_point2}))"
                    latex_expr += f"--((1-t)((1-t){control_point1}+t{control_point2})+t((1-t){control_point2}+t{end_point}))"
                start = end_point
            latex.append(latex_expr)
            print("Latex expression:", latex_expr)  # Print LaTeX expression for debugging
    return latex

get_latex("C:\\Users\\Willi\\OneDrive\\Documents\\GitHub\\desmos.ai-1\\src\\images\\temp_image.png")

def get_expressions(filename):
    exprid = 0
    exprs = []
    for expr in get_latex(filename):
        exprid += 1
        exprs.append({'latex': expr})
    return exprs

# Test:
# test_img_path =  "C:\\Users\\Willi\\OneDrive\\Documents\\GitHub\\desmos.ai-1\\src\\images\\temp_image.png"
# print(get_expressions(test_img_path))
