from sklearn.base import BaseEstimator, TransformerMixin
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import re
import pandas as pd



class TextCleaner(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))
        self.stop_words.difference_update({"not", "no", "don't", "never"})
        self.lemmatizer = WordNetLemmatizer()

    def clean(self, text):
        if not isinstance(text, str): return ""
        text = text.lower()
        text = re.sub(r'http\S+|www\.\S+', '', text)
        text = re.sub(r'\|\|\|', ' ', text)
        text = text.translate(str.maketrans('', '', string.punctuation))
        words = [w for w in text.split() if w not in self.stop_words]
        words = [self.lemmatizer.lemmatize(w) for w in words]
        return ' '.join(words)

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        # Handles both pandas Series and Python list
        return pd.Series(X).apply(self.clean)