# Handwritten Digit Recognition System

This project provides a Flask-based RESTful API for real-time handwritten digit recognition using a CNN model trained on the MNIST dataset.

## Features
- Upload an image of a handwritten digit for real-time recognition.
- Deployed on AWS EC2 for global accessibility.
- Future enhancements: alphanumeric recognition, mobile integration, and real-time handwriting conversion.

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Ketan-Chaudhary/deci-engine.git


2. Repository Structure
    ```bash
    flask-app/
    │
    ├── app.py                 # Main Flask application
    ├── model.h5               # Your machine learning model weights
    ├── model.json             # Your model architecture
    ├── templates/             # HTML templates
    │   └── index.html
    │   └── result.html
    ├── requirements.txt       # Python dependencies
    └── venv/                  # Virtual environment

4. Install dependencies:
   ```bash
    pip install -r requirements.txt


5. Run the Flask app:
   ```bash
    python app.py

6. Access the API at
   ```bash
      http://127.0.0.1:5000/predict.
   

6.API Usage
  POST /predict: Upload an image file to get the predicted digit in JSON format.
  
7.Future Work
  1. Alphanumeric character recognition.
  2.Mobile application integration.
  3.Real-time handwriting conversion.
