# Dimension-analysis-using-OpenCV-
# Dimension analysis using OpenCV and Python
This code provides a Python script for measuring properties of objects, such as diameter by detecting contours in images. It is particularly tailored towards analyzing circular shapes, e.g., gauges, using edge detection and circle fitting techniques. The contour with the maximum length is selected for measurement, and this selection's diameter is computed and displayed on the image.

# Features
Contour Detection: Detects the contours in an image using Canny edge detection.
Circle Fitting: Applies the Hyper Least Squares method to fit a circle around the detected contour.
Measurement: Calculates the diameter of the fitted circle in physical units (based on predefined pixel-per-unit ratios).
Result Visualization: Annotates the original image with the diameter of the detected contour and displays it.

# Dependencies
Python 3.x
OpenCV (cv2)
NumPy
A module named circle_fit which should contain a method hyperLSQ

Ensure all dependencies are installed using pip:
# pip install numpy
# pip install circle-fit

# Usage 
Place your images in a specified directory within the same directory as the script.

  Run the script:
  python <filename>.py

The script processes all images in the gauge directory, calculates the diameters of the detected contours, and displays the images with the diameter annotated. It also prints the maximum, mean, and mode of the diameters of all processed images to the console.
The mean, mode calculation is for identifying bias and variance in the results of images taken at a time.

# Contribution guidelines
Contributions are welcome! If you have improvements or bug fixes, please open a pull request. For major changes, please open an issue first to discuss what you would like to change.

# Acknowledgments 
All the libraries and functionalities have been used in this work is open-source!. 
