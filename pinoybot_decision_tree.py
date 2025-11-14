import pickle
import pandas as pd
import numpy as np
from feature_conversion import *
from helpers import *
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report
from sklearn.model_selection import train_test_split

# Converts csv into dataframe
annotations = pd.read_csv("final_annotations.csv")

an_words = annotations['word'].to_list()
an_words_labels = annotations['label'].to_list()
an_words_features = []
an_words_label_int = []

# Get features of words
for w in an_words:
    an_words_features.append(create_features(w))

# Convert labels to integer representations
for l in an_words_labels:
    an_words_label_int.append(label_to_int(l))

X = np.array(an_words_features)
Y = np.array(an_words_label_int)

# Training set: 70%
X_train, X_temp, Y_train, Y_temp = train_test_split(X, Y, test_size=0.30)

# Split 30% in half: 15% for testing, 15% for validation
X_val, X_test, Y_val, Y_test = train_test_split(X_temp, Y_temp, test_size=0.5)

# creating models with different depths
depths = [i for i in range(10,27)]
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
# model = DecisionTreeClassifier()
model.fit(X_train, Y_train)

importances = model.feature_importances_
print("Feature importances:", importances)

y_test_pred = model.predict(X_test)
accuracy = accuracy_score(Y_test, y_test_pred)

# CM: Confusion Matrix
cm = [[0 for _ in range(3)] for _ in range(3)]

for i in range(len(y_test_pred)):
    cm[Y_test[i]][y_test_pred[i]] += 1

print("="*60)
print("CONFUSION MATRIX")
print("="*60)
print()
print('                           PREDICTED')
print()
print('                    FIL       ENG       OTH')
print()
print(f'L        FIL{cm[0][0]:>11}{cm[0][1]:>10}{cm[0][2]:>10}')
print(f'A        ENG{cm[1][0]:>11}{cm[1][1]:>10}{cm[1][2]:>10}')
print(f'B        OTH{cm[2][0]:>11}{cm[2][1]:>10}{cm[2][2]:>10}')
print()

print("="*60)
print("DETAILED CLASSIFICATION REPORT")
print("="*60)

target_names = ['FIL', 'ENG', 'OTH']
print(classification_report(Y_test, y_test_pred, target_names=target_names, digits=2))
print("="*60)

filename = 'pinoybot_decision_tree.pkl'
with open(filename, 'wb') as file:
    pickle.dump(model, file)

print("Model saved!")