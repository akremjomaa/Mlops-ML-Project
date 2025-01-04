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

from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
import joblib

# Charger le jeu de données Iris
data = load_iris()
X = data.data
y = data.target

# Diviser le dataset en ensemble d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Définir les hyperparamètres à tester
param_grid = {
    'n_estimators': [50, 100, 200],  # Nombre d'arbres
    'max_depth': [None, 10, 20],  # Profondeur maximale des arbres
    'min_samples_split': [2, 5, 10],  # Nombre minimum d'échantillons nécessaires pour scinder un nœud
    'min_samples_leaf': [1, 2, 4]  # Nombre minimum d'échantillons dans chaque feuille
}

# Créer un modèle RandomForest
model = RandomForestClassifier(random_state=42)

# Appliquer GridSearchCV pour tester différentes combinaisons d'hyperparamètres
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5)  # cv=5 pour 5-fold cross-validation

# Entraîner le modèle avec la recherche sur la grille
grid_search.fit(X_train, y_train)

# Afficher les meilleurs hyperparamètres trouvés par GridSearchCV
print(f"Meilleurs hyperparamètres : {grid_search.best_params_}")

# Utiliser le meilleur modèle trouvé pour faire des prédictions sur l'ensemble de test
best_model = grid_search.best_estimator_

# Évaluer le modèle
accuracy = best_model.score(X_test, y_test)
print(f"Précision sur l'ensemble de test : {accuracy * 100:.2f}%")

# Sauvegarder le modèle
joblib.dump(best_model, 'server/iris_classification_model.pkl')
print("Modèle entraîné et sauvegardé sous iris_classification_model.pkl")

