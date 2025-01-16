
# Tree Classifier - AI-based Plant Classification

## Overview
Tree Classifier is a web application built using **Flask** as the backend and **TensorFlow** for the AI-based classification of plants. It uses machine learning models to classify plant species based on certain features of the plant's leaf.

## Features
- **Flask Backend**: The backend is built using Flask, providing RESTful APIs for plant classification.
- **AI-based TensorFlow Model**: The AI model is built using TensorFlow, trained on plant leaf features to classify three species: **Senna spectabilis**, **Senna siamea**, and **Cassia roxburghii**.
- **Interactive Web Interface**: Users can input plant features through a web form, and the model predicts the plant species along with the prediction confidence.

## Technologies Used
- **Flask**: Web framework for backend development.
- **TensorFlow**: Machine Learning framework for building the classification model.
- **HTML, CSS (Tailwind)**: For the frontend design of the web application.
- **JavaScript (GSAP)**: For animations on the frontend.

## Setup Instructions

### Prerequisites
1. Python 3.x
2. Flask
3. TensorFlow
4. Other Python dependencies

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Tree-Classifier.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Tree-Classifier
   ```

3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scriptsctivate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Run the Flask app:
   ```bash
   python app.py
   ```

7. The application will be accessible at `http://127.0.0.1:5000/`.

## Usage
- Visit the web interface.
- Enter the required leaf features (Rachis Length, Width, Length, Pair of Leaves).
- Click "Predict" to get the plant species prediction along with the confidence level.

## Contributing
Feel free to fork the repository, submit issues, and contribute improvements to the codebase. Please make sure to follow the contributing guidelines when submitting pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- The TensorFlow model used for classification was trained using plant leaf data.
- Tailwind CSS for the beautiful and responsive design.
