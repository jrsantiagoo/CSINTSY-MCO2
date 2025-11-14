import os
import pickle
import pandas as pd
import numpy as np
from feature_conversion import *
from helpers import *
from sklearn.naive_bayes import ComplementNB
from sklearn.metrics import accuracy_score 
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

X_train, X_temp, Y_train, Y_temp = train_test_split(X, Y, test_size=0.30)
X_val, X_test, Y_val, Y_test = train_test_split(X_temp, Y_temp, test_size=0.5)

# creating models with different depths
depths = [i for i in range(10,23)]
val_scores = []

# creating a model based on the best depth
model = ComplementNB()
model.fit(X_train, Y_train)
y_test_pred = model.predict(X_test)
accuracy = accuracy_score(Y_test, y_test_pred)
print(f"Bot accuracy: {accuracy:.3f}")

filename = 'pinoybot_complement_naive_bayes.pkl'
with open(filename, 'wb') as file:
    pickle.dump(model, file)

print("Model saved!")
