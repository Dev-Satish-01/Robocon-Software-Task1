import cv2
import numpy as np

def detect_arrow_angle(image_path):
    img = cv2.imread("Arrow_2.jpg", cv2.IMREAD_GRAYSCALE)

    # Apply threshold to get binary image
    _, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

    # Find contours in the binary image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter out small contours
    contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 100]

    # Get the angle based on the orientation of the arrow's major axis
    if contours:
        cnt = contours[0]
        angle = "Unknown"

        # Fit an ellipse to the contour
        ellipse = cv2.fitEllipse(cnt)
        major_axis_angle = ellipse[2]

        # Calculate the angle with respect to the positive X-axis
        angle = (90 - major_axis_angle) % 360

    return angle

if __name__ == "__main__":
    input_image_path = "Arrow_2.jpg"
    angle = detect_arrow_angle(input_image_path)
    
    if angle != "Unknown":
        print("Arrow Angle:", angle)
    else:
        print("Unable to detect arrow angle.")
