from django.apps import AppConfig
import pickle
from django.conf import settings
import os

class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
    # loading model
    count_path = os.path.join(settings.MODELS_ROOT, 'count_vectorizer.pkl')
    tfidf_path = os.path.join(settings.MODELS_ROOT, 'tfidf_transformer.pkl')
    pac_path = os.path.join(settings.MODELS_ROOT, 'pac.pkl')

    count_vectorizer = pickle.load(open(count_path, 'rb'))
    tfidf_transformer = pickle.load(open(tfidf_path, 'rb'))
    # Passive Aggressive Classifier
    pac = pickle.load(open(pac_path, 'rb'))

