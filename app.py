from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np

app = Flask(__name__)

# Load your trained model
model = tf.keras.models.load_model("best_model.keras")

# Classes
classes = ["Senna spectabilis", "Senna siamea", "Cassia roxburghii"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    print("Received data:", data)  # Debugging line to check the data being received

    try:
        # Extract input features
        rachis_length = data.get('Rachis Length', None)
        width = data.get('Width', None)
        length = data.get('Length', None)
        pair_of_leaves = data.get('Pair of Leaves', None)

        # Check for missing or invalid data
        if None in [rachis_length, width, length, pair_of_leaves]:
            return jsonify({"error": "Please provide valid input for all fields"}), 400

        # Convert to float or int if necessary
        rachis_length = float(rachis_length)
        width = float(width)
        length = float(length)
        pair_of_leaves = int(pair_of_leaves)

        # Calculate Width/Length Ratio
        width_length_ratio = width / length

        # Prepare input for the model
        input_data = np.array([[rachis_length, width_length_ratio, pair_of_leaves]])
        prediction = model.predict(input_data)
        class_idx = np.argmax(prediction)
        confidence = prediction[0][class_idx] * 100  # Confidence in percentage

        response = {
            "predicted_class": classes[class_idx],
            "confidence": f"{confidence:.2f}%"
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": f"Error processing the input data: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True)
