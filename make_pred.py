import pickle

def make_prediction(x):
    with open('main_model.pkl', 'rb') as fichier_modele:
        loaded_model = pickle.load(fichier_modele)

    predictions_out = loaded_model.predict(x)

    print('prediction:', predictions_out)

    # predictions_string = [str(int(predictions_out))]

    return str(int(predictions_out))
