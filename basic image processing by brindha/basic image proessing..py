import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Use tkinter to select image file
Tk().withdraw()  # Hide the root window
image_path = askopenfilename(title="Select an image file", filetypes=[("Image files", "*.jpg *.png *.jpeg *.bmp")])

# Load the image
img = cv2.imread(image_path)

if img is None:
    print(f"Error: Could not load image '{image_path}'")
else:
    # Display original image
    cv2.imshow("Original Image", img)

    # Cropping
    x, y, w, h = 100, 50, 200, 150
    cropped_img = img[y:y+h, x:x+w]
    cv2.imshow("Cropped Image", cropped_img)

    # Resizing
    resized_img = cv2.resize(img, (300, 200))
    cv2.imshow("Resized Image", resized_img)

    # Thresholding
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh_img = cv2.threshold(gray_img, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow("Thresholded Image", thresh_img)

    # Contour Analysis
    contours, _ = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour_img = img.copy()
    cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)
    cv2.imshow("Contour Image", contour_img)

    # Blob Detection
    params = cv2.SimpleBlobDetector_Params()
    params.filterByArea = True
    params.minArea = 100
    detector = cv2.SimpleBlobDetector_create(params)
    keypoints = detector.detect(gray_img)
    blob_img = cv2.drawKeypoints(img, keypoints, np.array([]), (0, 0, 255),
                                 cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow("Blob Detection", blob_img)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()
