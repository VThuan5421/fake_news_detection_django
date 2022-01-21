from django.shortcuts import render, redirect, HttpResponse
from app.apps import AppConfig
import re
import nltk
nltk.download('omw-1.4')
nltk.download('stopwords')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
from nltk.corpus import stopwords
stopwords = set(stopwords.words('english'))
# Create your views here.

def index(request):
    return render(request, "index.html")

def detect(request):
    if request.method == "POST":
        txt = request.POST['text']
        if len(txt) < 5:
            return render(request, "detect.html")
        base_text = preprocess_text(txt)
        # Transform text to count vectorizer
        count_vect = AppConfig.count_vectorizer.transform([base_text])
        # Transform count_vect to tf-idf transformer
        tfidf_trans = AppConfig.tfidf_transformer.transform(count_vect)
        # Time to predict and get result
        # Intialize Passive Aggressive Classifier model
        pac = AppConfig.pac
        result = pac.predict(tfidf_trans)[0]
        #print(result)
        #print(txt)
        return render(request, "detect.html", {"check_text": True, "txt": txt, 
            "check_result": True, 'result': result})

    return render(request, "detect.html")

def preprocess_text(x):
    # Convert to latin character, digit, space
    cleaned_text = re.sub(r'[^a-zA-Z\d\s\']+', '', x)
    # Split each word in the sentence
    word = nltk.word_tokenize(cleaned_text)
    # Stem each word, create base word (ex: went -> go)
    word_list = [lemmatizer.lemmatize(w.lower()) for w in word if w not in stopwords]
    return " ".join(word_list)



