import os
import joblib
import torch
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


model = torch.load('best3.pt', weights_only=False)
print(model)

#Load model from the new models folder
#MODEL_PATH = os.path.join("models", "random_forest_model.pkl")
#model = joblib.load(MODEL_PATH)

@app.route('/')
def index():
    return render_template('plant.html')
@app.route('/fertilizer.html')
def fertilizer():
    return render_template('fertilizer.html')
@app.route('/yield.html')
def render_yield():
    return render_template('yield.html')
@app.route('/disease.html')
def disease():
    return render_template('disease.html')
@app.route('/crop.html')
def crop():
    return render_template('crop.html')
@app.route('/chatbot.html')
def chatbot():
    return render_template('chatbot.html')
@app.route('/plant.html')
def plant():
    return render_template('plant.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

