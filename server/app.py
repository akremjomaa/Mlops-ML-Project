from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np

# Charger le modèle pré-entrainé
model = joblib.load("iris_classification_model.pkl")

# Définir le modèle de données (les features du dataset Iris)
class Features(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# Créer l'instance FastAPI
app = FastAPI()

@app.post("/predict")
def predict(features: Features):
    try:
        # Préparer les données pour la prédiction
        X_new = np.array([[features.sepal_length, features.sepal_width, features.petal_length, features.petal_width]])

        # Prédire la classe
        prediction = model.predict(X_new )
        
        # Retourner la classe prédite
        return {"prediction": int(prediction[0])}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
