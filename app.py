from flask import Flask, request, render_template, jsonify
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import model_from_json
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import io


app = Flask(__name__)

# Load the model architecture from model.json
with open('model.json', 'r') as json_file:
    model_json = json_file.read()

model = model_from_json(model_json)

# Load the model weights from model.h5
model.load_weights('model.h5')


# Routes
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', error="No file provided"), 400

        file = request.files['file']

        try:
            # Load the image and preprocess it
            image = Image.open(io.BytesIO(file.read())).convert('L')  # Convert to grayscale
            image = image.resize((28, 28))  # Resize to 28x28 pixels
            image = img_to_array(image)  # Convert to array
            image = np.expand_dims(image, axis=0)  # Add batch dimension
            image = image / 255.0  # Normalize to [0, 1]

            # Make a prediction
            predictions = model.predict(image)
            predicted_digit = np.argmax(predictions)

            # Render the result in the template
            return render_template('index.html', prediction=predicted_digit, confidences=predictions[0].tolist())

        except Exception as e:
            return render_template('index.html', error=str(e)), 500

    # Render the page for GET requests (i.e., when visiting the page)
    return render_template('index.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5100)



