import os
import numpy as np
from PIL import Image
import cv2

def preprocess_image(image_path):
    image = Image.open(image_path)
    image = image.resize((256, 256))  # Resize to the required input size
    image = np.array(image) / 255.0  # Normalize pixel values to [0, 1]
    return image

def preprocess_and_save_images(input_directory, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for subdir, _, files in os.walk(input_directory):
        for filename in files:
            if filename.endswith(".jpg") or filename.endswith(".png"):
                image_path = os.path.join(subdir, filename)
                save_path = os.path.join(output_directory, os.path.relpath(image_path, input_directory))
                os.makedirs(os.path.dirname(save_path), exist_ok=True)
                image = preprocess_image(image_path)
                cv2.imwrite(save_path, image * 255)  # Convert back to [0, 255] for saving

# Preprocess all images in the sentinel2 directories
preprocess_and_save_images("data/sentinel2/lombardia/data2016", "data/sentinel2/lombardia_preprocessed/2016")
preprocess_and_save_images("data/sentinel2/lombardia-classes", "data/sentinel2/lombardia-classes_preprocessed")
preprocess_and_save_images("data/sentinel2/lombardia2", "data/sentinel2/lombardia2_preprocessed")
preprocess_and_save_images("data/sentinel2/lombardia3", "data/sentinel2/lombardia3_preprocessed")
