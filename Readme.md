# ✈️ Volarus — Flight Delay Prediction

## 1. Présentation du projet

Volarus est un projet d'intelligence artificielle qui vise à prédire les retards de vols à l'aide du Machine Learning.

Le système prédit si un vol risque d'avoir au moins 15 minutes de retard et estime la probabilité de retard.

## 2. Technologies utilisées

- **Python** — langage de programmation
- **Pandas / NumPy** — manipulation des données
- **Scikit-learn** — entraînement du modèle
- **Random Forest** — modèle de prédiction
- **MLflow / DagsHub** — suivi des expériences et gestion du modèle
- **FastAPI** — création de l'API
- **Docker** — conteneurisation de l'application
- **Render** — hébergement de l'API

## 3. Architecture

```text
Volarus
│
├── Dataset/
│   └── Données utilisées pour l'entraînement
│
├── Documentation/
│
├── Livrable_MLFlow/
│
└── Volarus_Deployment/
    ├── app/
    │   ├── main.py
    │   ├── schemas.py
    │   └── static/
    │       └── index.html
    ├── models/
    ├── tests/
    ├── Dockerfile
    ├── requirements.txt
    └── .dockerignore
```

## 4. Modèle de Machine Learning

Le modèle sélectionné est un **Random Forest Classifier**.

Il utilise 15 variables d'entrée relatives au vol pour prédire si celui-ci risque d'être retardé d'au moins 15 minutes.

Métriques obtenues lors de l'évaluation :

| Métrique | Résultat |
|---|---:|
| Accuracy | 57,44 % |
| F1-score | 0,3328 |
| ROC-AUC | 0,6139 |
| Precision | 0,2288 |
| Recall | 0,6108 |

## 5. API publique

L'application est déployée sur Render.

- **Application :** https://projet-pr-diction-avion-retard.onrender.com
- **Documentation Swagger :** https://projet-pr-diction-avion-retard.onrender.com/docs
- **Health check :** https://projet-pr-diction-avion-retard.onrender.com/health
- **Model readiness :** https://projet-pr-diction-avion-retard.onrender.com/ready

### Endpoint de prédiction

`POST /predict`

L'API reçoit les 15 variables du vol au format JSON et retourne :

- La prédiction (0 ou 1).
- Une description du résultat.
- La probabilité estimée de retard.
- La source du modèle utilisé.

## 6. Exécution locale avec Docker

Prérequis : Docker Desktop.

Depuis le dossier `Volarus_Deployment` :

```bash
docker build -t volarus-api .
```

Lancer le conteneur :

```bash
docker run -p 8000:8000 --name volarus-container volarus-api
```

Accéder à la documentation :

http://localhost:8000/docs

## 7. Déploiement

L'API
