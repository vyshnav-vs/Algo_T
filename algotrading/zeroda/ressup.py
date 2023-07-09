import numpy as np
from skimage import io, color, filters, feature
# Load the image
image = io.imread('/home/vyshnav-vs/Desktop/algotrading/zeroda/cub.jpg')
# Check the number of channels in the image
num_channels = image.shape[2]

# Convert the image to RGB if it has four channels (RGBA)
if num_channels == 4:
    image = color.rgba2rgb(image)

# Convert the image to grayscale
image_gray = color.rgb2gray(image)

# Apply any necessary filters or adjustments
# For example, you can use a Gaussian blur to reduce noise
image_blur = filters.gaussian(image_gray, sigma=1.5)
# Apply the Canny edge detector
edges = feature.canny(image_blur, sigma=1.0, low_threshold=0.1, high_threshold=0.2)
# Perform Hough line detection
lines = feature.peak_local_max(feature.hough_line(edges), min_distance=20)

# Convert the lines to slope-intercept form (y = mx + c)
line_equations = []
for r, theta in lines:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * r
    y0 = b * r
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))
    line_equations.append((x1, y1, x2, y2))
# Find the intersections of the detected lines
intersections = []
for i in range(len(line_equations)):
    for j in range(i + 1, len(line_equations)):
        x1, y1, x2, y2 = line_equations[i]
        x3, y3, x4, y4 = line_equations[j]
        denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if denominator != 0:
            x = ((x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)) / denominator
            y = ((x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)) / denominator
            intersections.append((x, y))
# Perform further analysis on the intersections
# You can consider factors like frequency, proximity to price movements, etc.
# Identify the most significant support and resistance levels based on your criteria

# Example: Print the detected intersections
for intersection in intersections:
    print("Intersection coordinates: ", intersection)
