import cv2
import numpy as np
import glob
import os
import datetime


## Sharpen_image
def sharpen_image(image, size=1.0):
    # Create a sharpening kernel
    kernel = np.array([[-1, -1, -1], [-1, 9 + size, -1], [-1, -1, -1]])

    # Apply the kernel to the image using convolution
    sharpened_image = cv2.filter2D(image, -1, kernel)

    return sharpened_image


for img in glob.iglob("./images/*", recursive=True):
    if os.path.isdir(img):
        continue

    # Load the image
    image = cv2.imread(img)

    # sharpening image
    sharpened_image = sharpen_image(image, 0.1)
    adjusted_image = cv2.convertScaleAbs(sharpened_image, alpha=1.1, beta=0.1)

    path = img.split("/")[-1]
    # Save the sharpened image
    cv2.imwrite(f"./results/{path}", adjusted_image)
