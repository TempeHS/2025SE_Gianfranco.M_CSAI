from flask import Flask, render_template, request
from model import predict_round, encode_map

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        map_name = request.form['map_name']
        ct_money = float(request.form['ct_money'])
        t_money = float(request.form['t_money'])
        ct_alive = int(request.form['ct_alive'])
        t_alive = int(request.form['t_alive'])
        bomb_planted = int(request.form['bomb_planted'])

        map_encoded = encode_map(map_name)
        if map_encoded is None:
            return render_template('index.html', error="Map not found in training data.")

        input_dict = {
            'map': map_encoded,
            'ct_money': ct_money,
            't_money': t_money,
            'ct_players_alive': ct_alive,
            't_players_alive': t_alive,
            'bomb_planted': bomb_planted
        }

        result = predict_round(input_dict)
        return render_template('result.html', result=result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8888)