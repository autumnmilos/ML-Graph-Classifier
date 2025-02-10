# ML-Graph-Classifier

## Overview
GraphSourceDetector is a machine learning-based tool that extracts graphs from research papers (PDFs) and identifies the software used to generate them (e.g., Matplotlib, Excel, Seaborn, etc.).

## Features
- Extract images from PDFs automatically
- Preprocess and classify graphs vs. non-graph images
- Identify the source visualization tool used to generate graphs
- Trainable ML model for better accuracy

## Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/GraphSourceDetector.git
cd GraphSourceDetector

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

## Usage
### 1. Extract Images from PDFs
```bash
python extract_images.py --pdf_folder input_papers/ --output_folder extracted_images/
```

### 2. Preprocess Images
```bash
python preprocess_images.py --input_folder extracted_images/ --output_folder processed_images/
```

### 3. Train the Model
```bash
python train_model.py --dataset processed_images/ --epochs 10
```

### 4. Predict Visualization Tool from an Image
```bash
python predict.py --image sample_graph.png
```

## Folder Structure
```
GraphSourceDetector/
│── input_papers/        # Folder to store research papers (PDFs)
│── extracted_images/    # Folder to store extracted images
│── processed_images/    # Folder for preprocessed images
│── models/              # Trained ML models
│── extract_images.py    # Script to extract images from PDFs
│── preprocess_images.py # Script for preprocessing images
│── train_model.py       # Train the ML model
│── predict.py           # Predict visualization tool
│── requirements.txt     # Dependencies
│── README.md            # Project documentation
```

## Dependencies
- Python 3.x
- OpenCV
- PyMuPDF
- TensorFlow/Keras (for deep learning model)
- Scikit-learn
- Matplotlib

## Contributing
Feel free to fork and contribute by submitting a pull request.


