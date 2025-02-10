import cv2
import os
import argparse

def preprocess_image(image_path, output_path):
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    img_resized = cv2.resize(img, (224, 224))
    cv2.imwrite(output_path, img_resized)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_folder", required=True)
    parser.add_argument("--output_folder", required=True)
    args = parser.parse_args()
    
    os.makedirs(args.output_folder, exist_ok=True)
    for img_file in os.listdir(args.input_folder):
        input_path = os.path.join(args.input_folder, img_file)
        output_path = os.path.join(args.output_folder, img_file)
        preprocess_image(input_path, output_path)

if __name__ == "__main__":
    main()
