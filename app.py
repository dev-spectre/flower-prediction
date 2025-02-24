from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
  sepal_width = request.form.get("Sepal_Width")
  petal_width = request.form.get("Petal_Width")
  sepal_length = request.form.get("Sepal_Length")
  petal_length = request.form.get("Petal_Length")
  
  x = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
  y = model.predict(np.array(x))
  
  return render_template('index.html', prediction_text=y[0])

if __name__ == "__main__":
  app.run(debug=True)