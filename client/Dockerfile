# Utiliser une image Python officielle
FROM python:3.9-slim

# Copier le fichier de dépendances et l'installer
COPY requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port de Streamlit
EXPOSE 8501

# Copier l'application Streamlit
COPY app.py app.py
COPY images images


# Lancer Streamlit
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
