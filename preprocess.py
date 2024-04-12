import token
import pandas as pd
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
nltk.download('stopwords')
import string 
from nltk.stem import PorterStemmer

s1 = stopwords.words ('english')
ps = PorterStemmer()

def stop(text):
    y = [i for i in text if i not in s1]
    return y

def preprocess(text):

    lower_text = text.lower()
    # print("Lower text: " ,lower_text)
    tokenized_text = nltk.word_tokenize(lower_text)
    # print("Tokenize text: " ,tokenized_text)
    stop_text = stop(tokenized_text)
    # print("Stop text: " ,stop_text)
    punc_text = [i for i in stop_text if i not in string.punctuation]
    # print("Punc text: " ,punc_text)
    stem_tex = [ps.stem(i) for i in punc_text]
    # print("Stemed text: " ,stem_tex)
    return stem_tex


if __name__ == "__main__":
    preprocess("I am Anupam ! I am a good currenlty working in a company.")
    pass