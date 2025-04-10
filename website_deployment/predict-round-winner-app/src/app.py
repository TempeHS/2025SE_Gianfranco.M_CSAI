from flask import Flask, request, render_template
from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

app = Flask(__name__)

scaler = preprocessing.StandardScaler()
label_encoder = preprocessing.LabelEncoder()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    map_name = request.form['map_name']
    ct_money = float(request.form['ct_money'])
    t_money = float(request.form['t_money'])
    ct_players_alive = int(request.form['ct_players_alive'])
    t_players_alive = int(request.form['t_players_alive'])
    bomb_planted = int(request.form['bomb_planted'])

    prediction = model_handler.predict_winner(map_name, ct_money, t_money, ct_players_alive, t_players_alive, bomb_planted)
    return render_template('index.html', prediction=prediction)

@app.route('/train', methods=['GET', 'POST'])
def train():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            model_handler.retrain_model(file)
            return render_template('train.html', message="Model retrained successfully!")
    return render_template('train.html')

if __name__ == '__main__':
    app.run(debug=True)