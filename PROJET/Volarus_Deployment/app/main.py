
from fastapi import FastAPI, HTTPException
from pathlib import Path
import joblib
import pandas as pd

from app.schemas import FlightInput
from fastapi.responses import FileResponse

app = FastAPI(
    title="Volarus API",
    description="API de prédiction des retards de vols",
    version="1.0.0"
)

@app.get("/")
def home():
    return FileResponse(
        Path(__file__).parent / "static" / "index.html"
    )

# Chargement du modèle depuis les fichiers locaux
MODEL_DIR = Path(__file__).resolve().parent.parent / "models"

model = joblib.load(
    MODEL_DIR / "volarus_best_random_forest.pkl"
)

encoder = joblib.load(
    MODEL_DIR / "volarus_encoder.pkl"
)

model_source = "Fichiers locaux"

print("Modèle local chargé avec succès !")


@app.get("/health")
def health_check():
    return {
        "status": "OK",
        "message": "Volarus API fonctionne correctement"
    }


@app.get("/ready")
def ready_check():
    return {
        "status": "ready",
        "model_source": model_source,
        "message": "Le modèle Volarus est chargé."
    }


@app.post("/predict")
def predict_flight(flight: FlightInput):

    try:
        input_df = pd.DataFrame([flight.model_dump()])

        # MLflow : le pipeline effectue lui-même le prétraitement
        if model_source == "MLflow / DagsHub":
            prediction = int(model.predict(input_df)[0])
            probabilities = model.predict_proba(input_df)[0]

        # Local : appliquer l'encodeur séparément
        else:
            encoded_data = encoder.transform(input_df)

            prediction = int(model.predict(encoded_data)[0])
            probabilities = model.predict_proba(encoded_data)[0]

        delay_probability = float(probabilities[1])

        return {
            "prediction": prediction,
            "result": (
                "Risque de retard d'au moins 15 minutes"
                if prediction == 1
                else "Vol probablement à l'heure"
            ),
            "delay_probability": round(delay_probability, 4),
            "model_source": model_source
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erreur lors de la prédiction : {str(e)}"
        )
