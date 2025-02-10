import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import argparse

def build_model():
    model = Sequential([
        Conv2D(32, (3,3), activation='relu', input_shape=(224,224,3)),
        MaxPooling2D(2,2),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(3, activation='softmax')  # Assuming 3 visualization tools
    ])
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", required=True)
    parser.add_argument("--epochs", type=int, default=10)
    args = parser.parse_args()
    
    datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)
    train_generator = datagen.flow_from_directory(args.dataset, target_size=(224,224), batch_size=32, class_mode='categorical', subset='training')
    val_generator = datagen.flow_from_directory(args.dataset, target_size=(224,224), batch_size=32, class_mode='categorical', subset='validation')
    
    model = build_model()
    model.fit(train_generator, validation_data=val_generator, epochs=args.epochs)
    model.save("models/graph_classifier.h5")

if __name__ == "__main__":
    main()
