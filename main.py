import cv2
import numpy as np
import os
from circle_fit import hyperLSQ
import statistics

# This pixel per ratio is calculated to convert pixel values in to realtime measurement mm

PIXEL_PER_RATIO = 0.0846 #basler
PIXEL_PER_RATIO = 0.0664 #logitech webcam 1080p

arr=[]

def detection(image_path):

    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)  # Replace with your image path

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (3, 3), 0) #This step is only recommended if your input image has more noise and distortion

    #Threshold value has been set by trial and error method

    t_lower = 60 # Lower Threshold 
    t_upper = 140 # Upper threshold


    # Apply Canny edge detection (Simple and efficient)
    edge = cv2.Canny(blurred, t_lower, t_upper) # This edge detection method has been chose by trial and error method

    # Find contours
    contours, _ = cv2.findContours(edge, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    #### The below (ROI)method is optional 

    avg = sum([cv2.contourArea(x) for x in contours]) / len(contours) 

    contours = [x for x in contours if cv2.contourArea(x) > 0.3 * avg] #This method is to eliminate small contours which are not likely to be circles aka to get region of interest
 
    ####

    longest_contour = max(contours, key=lambda cnt: cv2.arcLength(cnt, True)) #The bool represents the continuous contour has been closed or opened

    points = [x[0].tolist() for x in longest_contour]
    xc, yc, r, sigma = hyperLSQ(points) # get the radius

    
    diameter = r*2*PIXEL_PER_RATIO # Here the values are calculated in mm

    arr.append(diameter)

    # below both methods will return the results in the images
    cv2.circle(image, (int(xc), int(yc)), int(r), (0, 0, 255), 2)
    #cv2.drawContours(gray, longest_contour, -1, (0, 153, 0), 2)
    cv2.putText(image, 'dia: ' + str(diameter), (int(image.shape[1]/2), int(image.shape[0]/2)), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 2)
    
    return image
    
for image in os.listdir('guage'):
    detection('guage/' + image)


cv2.waitKey(0)
cv2.destroyAllWindows()

print('Results : ',arr)
max = max(arr)
mean = sum(arr)/len(arr)
mode = statistics.mode(arr)
print("Max : ", max )
print("Mean : ", mean)
print("mode", mode)


