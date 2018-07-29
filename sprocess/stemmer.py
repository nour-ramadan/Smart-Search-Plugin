from nltk.stem.isri import ISRIStemmer

class stemmer:

    def __init__(self):
        self.st = ISRIStemmer()

    def stem(self, word):
        return self.st.stem(word)