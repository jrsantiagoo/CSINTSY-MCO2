import os
import pickle
import pandas as pd
import numpy as np
from featureConversion import *
from helpers import *
from sklearn.tree import DecisionTreeClassifier
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

for d in depths:
    model = DecisionTreeClassifier(max_depth=d)
    model.fit(X_train, Y_train)
    y_val_pred = model.predict(X_val)
    accuracy = accuracy_score(Y_val, y_val_pred)
    val_scores.append(accuracy)

best_depth = depths[val_scores.index(max(val_scores))]
print(f"Best max_depth based on validation: {best_depth}")

# creating a model based on the best depth
model = DecisionTreeClassifier(max_depth=best_depth)
model.fit(X_train, Y_train)
y_test_pred = model.predict(X_test)
accuracy = accuracy_score(Y_test, y_test_pred)
print(f"Bot accuracy: {accuracy:.3f}")

filename = 'pinoybot_decision_tree.pkl'
with open(filename, 'wb') as file:
    pickle.dump(model, file)

print("Model saved!")
