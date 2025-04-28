import pandas as pd
import pickle

# Load scaler (jika diperlukan)
with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

def preprocess_input(data):
    # Buat DataFrame dari input
    df = pd.DataFrame([data.dict()])

    # Normalisasi (jika diperlukan)
    # Jika Anda sudah melakukan scaling saat training, Anda perlu scaling data input juga
    # df_scaled = scaler.transform(df) 
    # return df_scaled

    return df  # Kembalikan DataFrame tanpa scaling jika tidak diperlukan