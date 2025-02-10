import tensorflow as tf
import cv2
import numpy as np
import argparse

def predict(image_path, model_path):
    model = tf.keras.models.load_model(model_path)
    img = cv2.imread(image_path)
    img_resized = cv2.resize(img, (224, 224)) / 255.0
    img_expanded = np.expand_dims(img_resized, axis=0)
    predictions = model.predict(img_expanded)
    classes = ["Matplotlib", "Excel", "Seaborn"]
    print(f"Predicted visualization tool: {classes[np.argmax(predictions)]}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True)
    parser.add_argument("--model", default="models/graph_classifier.h5")
    args = parser.parse_args()
    predict(args.image, args.model)

if __name__ == "__main__":
    main()
