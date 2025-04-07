import pandas as pd
import joblib

def save_application(data):
    df = pd.DataFrame([data])
    df.to_csv('data/user_data.csv', mode='a', header=False, index=False)

def load_model():
    return joblib.load('loan_approval_model.joblib')
