
import joblib
from pathlib import Path

# Chemin du dossier contenant les modèles
MODEL_DIR = Path(__file__).parent / "models"

# Charger les trois fichiers
model = joblib.load(MODEL_DIR / "volarus_best_random_forest.pkl")
encoder = joblib.load(MODEL_DIR / "volarus_encoder.pkl")
feature_names = joblib.load(MODEL_DIR / "volarus_feature_names.pkl")

print("Modèle chargé :", type(model).__name__)
print("Encodeur chargé :", type(encoder).__name__)
print("Nombre de variables :", len(feature_names))
print("Chargement réussi !")
