# Utiliser une image Python officielle
FROM python:3.9-slim

# Copier le fichier de dépendances et l'installer
COPY requirements.txt /app/requirements.txt
WORKDIR /app 

RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port de l'API
EXPOSE 8000

# Copier l'ensemble du code
COPY app.py app.py
COPY iris_classification_model.pkl iris_classification_model.pkl

# Lancer l'API FastAPI avec Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
