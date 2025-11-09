import os
import pickle
import pandas as pd
import numpy as np
from featureConversion import *
from helpers import *
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from typing import List

# Converts csv into dataframe
annotations = pd.read_csv("final_annotations.csv")

an_words = annotations['word'].to_list()
an_words_labels = annotations['label'].to_list()
an_words_features = []
#an_words_label_int = []


for w in an_words:
    an_words_features.append(create_features(w))

#for l in an_words_labels:
#    an_words_label_int.append(label_to_int(l))

X = np.array(an_words_features)
Y = np.array(an_words_labels)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20)

model = DecisionTreeClassifier()

model.fit(X_train, Y_train)

filename = 'pinoybot_decision_tree.pkl'

with open(filename, 'wb') as file:
    pickle.dump(model, file)

print("Model saved!")
