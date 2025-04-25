import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Hide tkinter root window
Tk().withdraw()

# Open file dialog to select an image
image_path = askopenfilename(title="Select an image", filetypes=[("Image files", "*.jpg *.png *.jpeg *.bmp")])

if not image_path:
    print("No file selected.")
else:
    try:
        # Load the image
        img = cv2.imread(image_path)

        if img is None:
            print("Error: Could not open or read the image.")
        else:
            # Line (red)
            cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 0, 255), 3)

            # Rectangle (green)
            cv2.rectangle(img, (100, 100), (200, 200), (0, 255, 0), 2)

            # Filled Circle (blue)
            cv2.circle(img, (300, 150), 50, (255, 0, 0), -1)

            # Ellipse (cyan)
            cv2.ellipse(img, (450, 250), (50, 30), 0, 0, 360, (255, 255, 0), 2)

            # Text (purple)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, 'OpenCV Annotation', (10, 50), font, 1, (255, 0, 255), 2, cv2.LINE_AA)

            # Display annotated image
            cv2.imshow("Annotated Image", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            # Optional: Save output
            # cv2.imwrite("annotated_output.jpg", img)

    except Exception as e:
        print(f"An error occurred: {e}")
