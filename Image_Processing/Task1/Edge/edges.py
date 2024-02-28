from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def apply_edge_detection(image_path, output_path):
    img = Image.open("flower.jpg")
    img_array = np.array(img)

    # Convert the image to grayscale
    gray_img_array = np.mean(img_array, axis=-1)

    # Applying edge detection using Sobel filter
    sobel_filter_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    sobel_filter_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

    # Convolve image with Sobel filters
    gx = convolve2d(gray_img_array, sobel_filter_x, mode='same', boundary='symm')
    gy = convolve2d(gray_img_array, sobel_filter_y, mode='same', boundary='symm')

    gradient_magnitude = np.sqrt(gx**2 + gy**2)
    gradient_magnitude = np.clip(gradient_magnitude, 0, 255)

    # Apply edge threshold (adjust threshold as needed)
    edge_threshold = 80
    img_array[gradient_magnitude > edge_threshold] = [255, 255, 255]
    img_array[gradient_magnitude <= edge_threshold] = [0, 0, 0]

    edge_img = Image.fromarray(img_array.astype('uint8'))
    edge_img.save(output_path)

if __name__ == "__main__":
    input_image_path = "flower.jpg"
    output_image_path = "edges.jpg"

    apply_edge_detection(input_image_path, output_image_path)
