import os
import datetime
# importing OpenCV library
from cv2 import *


def take_photo() -> str:
    """
    This function is used to take a photo.

    Returns
    ------------------------------------------------------------------
        The path where the image was stored.
    """
    # program to capture single image from webcam in python

    # initialize the camera
    # If you have multiple camera connected with
    # current device, assign a value in cam_port
    # variable according to that
    cam_port = 0
    cam = VideoCapture(cam_port)

    # reading the input using the camera
    result, image = cam.read()

    # If image will detected without any error,
    # show result
    if result:

        # showing result, it take frame name and image
        # output
        #imshow("GeeksForGeeks", image)
        image_name = f'/server/src/{datetime.datetime.now()}.png'.replace(' ', '_')

        # saving image in local storage
        imwrite(image_name, image)

    # If captured image is corrupted, moving to else part
    else:
        print("No image detected. Please! try again")

    
    os.system(f'fswebcam --no-banner {image_name}')

    return image_name
