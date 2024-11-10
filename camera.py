import cv2

def process_camera(frame):
    # Convert the frame to LAB color space and apply Gaussian blur
    ImageLAB = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    blur = cv2.GaussianBlur(ImageLAB[:, :, 0], (3, 3), 0)
    
    # Apply threshold to create binary image
    _, Fg_thresh = cv2.threshold(blur, 115, 255, cv2.THRESH_BINARY)
    
    # Return the processed frame
    return Fg_thresh
