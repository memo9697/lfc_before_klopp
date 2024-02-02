# Importez les bibliothèques nécessaires
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import mean_absolute_error
import csv
import json
import pickle

# Chargez votre DataFrame
# Supposons que votre DataFrame s'appelle 'df' et a les colonnes 'score', 'temps_livraison', 'prix', 'retard_livraison'
# Assurez-vous d'adapter cela à votre propre structure de données
# Exemple :
# df = pd.read_csv("votre_fichier.csv")

# Séparez les données en variables explicatives (X) et la variable cible (y)

def make_model_save():

    olist_df = pd.read_csv("training_dataset.csv")

    X = olist_df[['temps_livraison', 'price']]
    y = olist_df['score']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(random_state=42)

    model.fit(X_train, y_train)

    with open('main_model.pkl', 'wb') as fichier_modele:
        pickle.dump(model, fichier_modele)

    predictions = model.predict(X_test)
    print(f"MAE: {str(mean_absolute_error(predictions, y_test))}")