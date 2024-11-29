from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Charger le jeu de données Iris
data = load_iris()
X = data.data
y = data.target

# Diviser le dataset en ensemble d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraîner un modèle RandomForest
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Sauvegarder le modèle
joblib.dump(model, 'iris_classification_model.pkl')
print("Modèle entraîné et sauvegardé sous iris_classification_model.pkl")
