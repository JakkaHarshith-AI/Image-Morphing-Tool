import cv2
import numpy as np

# Load images
img1 = cv2.imread("input1.jpg")
img2 = cv2.imread("input2.jpg")

if img1 is None or img2 is None:
    print("Error loading images")
    exit()

# Resize images to same size
height = min(img1.shape[0], img2.shape[0])
width = min(img1.shape[1], img2.shape[1])

img1 = cv2.resize(img1, (width, height))
img2 = cv2.resize(img2, (width, height))

# Blend images (simple morph)
alpha = 0.5
morphed = cv2.addWeighted(img1, alpha, img2, 1 - alpha, 0)

# Save output
cv2.imwrite("morphed_output.jpg", morphed)

# Display
cv2.imshow("Morphed Image", morphed)
cv2.waitKey(0)
cv2.destroyAllWindows()
