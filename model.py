import librosa
import numpy as np
import joblib

model = joblib.load("saved_model/model.pkl")

def extract_features(file_path):
    audio, sample_rate = librosa.load(file_path, res_type='kaiser_fast')

    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)

    mfccs_scaled = np.mean(mfccs.T, axis=0)

    return mfccs_scaled

def predict_audio(file_path):
    features = extract_features(file_path)

    features = features.reshape(1, -1)

    prediction = model.predict(features)

    if prediction[0] == 1:
        return "FAKE Voice"
    else:
        return "REAL Voice"