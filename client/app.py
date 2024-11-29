import streamlit as st
import requests

# URL de l'API FastAPI
SERVER_URL = "http://server:8000/predict"

# Dictionnaire des fleurs associées aux classes (à ajuster selon ton modèle)
flower_images = {
    0: "images/setosa.jpg",        # Iris-setosa
    1: "images/versicolor.jpg",    # Iris-versicolor
    2: "images/virginica.jpg"      # Iris-virginica
}

# Affichage de l'interface Streamlit
st.title("Prédiction de la fleur Iris")
st.write("Entrez les caractéristiques de la fleur Iris pour la prédiction")

# Créer des entrées pour chaque caractéristique (longueur/pétale, largeur/pétale, etc.)
sepal_length = st.number_input("Longueur du sépale", min_value=0.0, max_value=10.0, value=5.0)
sepal_width = st.number_input("Largeur du sépale", min_value=0.0, max_value=10.0, value=3.0)
petal_length = st.number_input("Longueur du pétale", min_value=0.0, max_value=10.0, value=1.5)
petal_width = st.number_input("Largeur du pétale", min_value=0.0, max_value=10.0, value=0.2)

# Quand l'utilisateur clique sur le bouton pour effectuer la prédiction
if st.button("Prédire"):
    # Construire la charge utile pour l'API
    payload = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }
    
    # Envoyer la requête à l'API FastAPI pour la prédiction
    response = requests.post(SERVER_URL, json=payload)
    
    if response.status_code == 200:
        result = response.json()
        prediction_class = result['prediction']
        if(prediction_class == 0):
            prediction_class_name = "Iris-setosa"
        elif(prediction_class == 1):
            prediction_class_name = "Iris-versicolor"
        else:
            prediction_class_name = "Iris-virginica"
        
        # Afficher le résultat de la prédiction
        st.write(f"**Prédiction**: La fleur est probablement {prediction_class_name}.")

        # Afficher l'image associée à la classe prédite
        if prediction_class in flower_images:
            st.image(flower_images[prediction_class], caption=f"{prediction_class_name}", width=400, use_container_width=True)
    else:
        st.error("Erreur lors de la prédiction. Veuillez réessayer.")
