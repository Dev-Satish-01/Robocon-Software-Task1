from PIL import Image
import numpy as np

def apply_blur(image_path, output_path):
    img = Image.open("hills.jpg")
    img_array = np.array(img)

    # Applying blur using nested for loop
    for i in range(1, img_array.shape[0] - 1):
        for j in range(1, img_array.shape[1] - 1):
            img_array[i, j] = np.mean(img_array[i-1:i+2, j-1:j+2], axis=(0, 1))

    blurred_img = Image.fromarray(img_array.astype('uint8'))
    blurred_img.save(output_path)

if __name__ == "__main__":
    input_image_path = "hills.jpg"
    output_image_path = "blurred.jpg"

    apply_blur(input_image_path, output_image_path)
