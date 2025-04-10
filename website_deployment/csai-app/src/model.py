import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('/workspaces/2025SE_Gianfranco.M_CSAI/website_deployment/predict-round-winner-app/src/static/csgo_round_snapshots.csv')

label_encoder = LabelEncoder()
df['round_winner'] = label_encoder.fit_transform(df['round_winner'])
df['bomb_planted'] = label_encoder.fit_transform(df['bomb_planted'])
df['map'] = label_encoder.fit_transform(df['map'])


X_columns = ['map', 'ct_money', 't_money', 'ct_players_alive', 't_players_alive', 'bomb_planted']
X = df[X_columns]
y = df['round_winner']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
rf_model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
rf_model.fit(X_train, y_train)

def predict_round(input_dict):
    input_df = pd.DataFrame([input_dict])
    input_df = input_df.reindex(columns=X_columns, fill_value=0)
    prediction = rf_model.predict(input_df)
    return "Counter-terrorists" if prediction[0] == 0 else "Terrorists"

def encode_map(map_name):
    if map_name in label_encoder.classes_:
        return label_encoder.transform([map_name])[0]
    else:
        return None
