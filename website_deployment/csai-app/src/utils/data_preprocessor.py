class DataPreprocessor:
    def __init__(self, label_encoders=None, scaler=None):
        self.label_encoders = label_encoders if label_encoders else {}
        self.scaler = scaler

    def fit(self, df, categorical_columns, numerical_columns):
        for column in categorical_columns:
            le = preprocessing.LabelEncoder()
            df[column] = le.fit_transform(df[column])
            self.label_encoders[column] = le
        self.scaler = preprocessing.StandardScaler().fit(df[numerical_columns])

    def transform(self, df):
        for column, le in self.label_encoders.items():
            df[column] = le.transform(df[column])
        numerical_columns = df.select_dtypes(include=['float64', 'int']).columns
        scaled_data = self.scaler.transform(df[numerical_columns])
        df[numerical_columns] = scaled_data
        return df

    def inverse_transform(self, df):
        for column, le in self.label_encoders.items():
            df[column] = le.inverse_transform(df[column])
        return df