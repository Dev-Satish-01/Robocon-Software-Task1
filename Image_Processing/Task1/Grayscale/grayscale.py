from PIL import Image
import numpy as np

def apply_grayscale(image_path, output_path):
    img = Image.open("bees.jpg")
    img_array = np.array(img)

    # Applying grayscale using nested for loop
    for i in range(img_array.shape[0]):
        for j in range(img_array.shape[1]):
            avg_value = int(np.mean(img_array[i, j]))
            img_array[i, j] = [avg_value, avg_value, avg_value]

    grayscale_img = Image.fromarray(img_array.astype('uint8'))
    grayscale_img.save(output_path)

if __name__ == "__main__":
    input_image_path = "bees.jpg"
    output_image_path = "grayscale.jpg"

    apply_grayscale(input_image_path, output_image_path)
