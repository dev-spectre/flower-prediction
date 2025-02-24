# Flower Prediction Flask App (Iris Dataset)

## Overview
This is a simple Machine Learning-powered web application built using Flask that predicts the species of a flower based on the Iris dataset. Users can input flower features such as sepal length, sepal width, petal length, and petal width, and the model will classify the species (Setosa, Versicolor, or Virginica).

## Features
- Built using Flask for the web framework
- Utilises a trained Machine Learning model (Random Forest)
- User-friendly web interface for input
- API endpoint for predictions

## Installation

### Prerequisites
Ensure you have Python installed (preferably 3.7 or later) and install the required dependencies.

### Steps
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/flower-prediction-flask.git
   cd flower-prediction-flask
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Flask app:
   ```sh
   python app.py
   ```
5. Open your browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## Usage
- Enter the sepal and petal measurements in the form provided.
- Click the "Predict" button to get the predicted flower species.
- API Usage:
  ```sh
  curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"Sepal_Length": 5.1, "Sepal_Width": 3.5, "Petal_Length": 1.4, "Petal_Width": 0.2}'
  ```

## Model
The ML model is trained on the Iris dataset, which contains 150 samples of iris flowers divided into three species. The model is saved using `pickle` and loaded during runtime.

## Directory Structure
```
flower-prediction-flask/
│── app.py            # Main Flask application
│── model.pkl         # Pre-trained ML model
│── templates/
│   ├── index.html    # Frontend HTML template
│── static/
│   ├── style.css     # CSS file for styling
│── requirements.txt  # Dependencies
│── README.md         # Project documentation
```

## Contributing
Feel free to fork the repo and submit pull requests with improvements.

## License
This project is licensed under the MIT License.

---

