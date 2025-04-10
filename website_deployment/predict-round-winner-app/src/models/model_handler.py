import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing

class ModelHandler:
    def __init__(self):
        # Initialize model, scaler, and label encoder
        self.model = RandomForestClassifier(n_estimators=100)
        self.scaler = preprocessing.StandardScaler()
        self.label_encoder = preprocessing.LabelEncoder()

        # Load and preprocess the dataset
        self.df = pd.read_csv('/workspaces/2025SE_Gianfranco.M_CSAI/1. Data/csgo_round_snapshots.csv')
        self.df['round_winner'] = self.label_encoder.fit_transform(self.df['round_winner'])
        self.df['bomb_planted'] = self.label_encoder.fit_transform(self.df['bomb_planted'])
        self.df['map'] = self.label_encoder.fit_transform(self.df['map'])

        # Split the data
        self.X = self.df.drop(columns=['round_winner'])
        self.y = self.df['round_winner']
        self.scaler.fit(self.X)

        # Train the model
        self.model.fit(self.X, self.y)

    def predict_winner(self, map_name, ct_money, t_money, ct_players_alive, t_players_alive, bomb_planted):
        # Encode the map name
        if map_name in self.label_encoder.classes_:
            map_encoded = self.label_encoder.transform([map_name])[0]
        else:
            raise ValueError("Invalid map name")

        # Prepare input data
        input_data = pd.DataFrame([{
            "ct_money": ct_money,
            "t_money": t_money,
            "ct_players_alive": ct_players_alive,
            "t_players_alive": t_players_alive,
            "map": map_encoded,
            "bomb_planted": bomb_planted
        }])
        input_data_scaled = self.scaler.transform(input_data)

        # Make prediction
        prediction = self.model.predict(input_data_scaled)
        winner = "Counter-Terrorists" if prediction[0] == 0 else "Terrorists"
        return winner

    def retrain_model(self, new_data_file):
        # Load new data and retrain the model
        new_df = pd.read_csv(new_data_file)
        new_df['round_winner'] = self.label_encoder.fit_transform(new_df['round_winner'])
        new_df['bomb_planted'] = self.label_encoder.fit_transform(new_df['bomb_planted'])
        new_df['map'] = self.label_encoder.fit_transform(new_df['map'])

        X_new = new_df.drop(columns=['round_winner'])
        y_new = new_df['round_winner']
        self.scaler.fit(X_new)
        self.model.fit(X_new, y_new)