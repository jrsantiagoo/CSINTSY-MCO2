import pickle
import pandas as pd
import numpy as np
from featureConversion import *
from helpers import *
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score 
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

# Creating models with different depths
depths = [i for i in range(10,27)]
val_scores = []

# Checking which max_depth can produce the best results
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

# CM: Confusion Matrix
cm = [[0 for _ in range(3)] for _ in range(3)]

for i in range(len(y_test_pred)):
    cm[Y_test[i]][y_test_pred[i]] += 1

predicted_fil = (cm[0][0] + cm[1][0] + cm[2][0])
predicted_eng = (cm[0][1] + cm[1][1] + cm[2][1])
predicted_oth = (cm[0][2] + cm[1][2] + cm[2][2])
label_fil = (cm[0][0] + cm[0][1] + cm[0][2])
label_eng = (cm[1][0] + cm[1][1] + cm[1][2])
label_oth = (cm[2][0] + cm[2][1] + cm[2][2])

# Precision
prec_fil = cm[0][0] / predicted_fil
prec_eng = cm[1][1] / predicted_eng
prec_oth = cm[2][2] / predicted_oth

# Recall
rec_fil = cm[0][0] / label_fil
rec_eng = cm[1][1] / label_eng
rec_oth = cm[2][2] / label_oth

# F1-Score
f1_fil = 2 * (prec_fil * rec_fil) / (prec_fil + rec_fil)
f1_eng = 2 * (prec_eng * rec_eng) / (prec_eng + rec_eng)
f1_oth = 2 * (prec_oth * rec_oth) / (prec_oth + rec_oth)

accuracy = (cm[0][0] + cm[1][1] + cm[2][2]) / len(y_test_pred)
w_avg_prec = prec_fil * (label_fil / len(y_test_pred)) + prec_eng * (label_eng / len(y_test_pred)) + prec_oth * (label_oth / len(y_test_pred))
w_avg_rec = rec_fil * (label_fil / len(y_test_pred)) + rec_eng * (label_eng / len(y_test_pred)) + rec_oth * (label_oth / len(y_test_pred))
w_avg_f1 = f1_fil * (label_fil / len(y_test_pred)) + f1_eng * (label_eng / len(y_test_pred)) + f1_oth * (label_oth / len(y_test_pred))

print()
print('                 Confusion Matrix')
print('                       PRED')
print('                FIL         ENG         OTH')
print(f'L  FIL {cm[0][0]:>12}{cm[0][1]:>12}{cm[0][2]:>12}')
print(f'A  ENG {cm[1][0]:>12}{cm[1][1]:>12}{cm[1][2]:>12}')
print(f'B  OTH {cm[2][0]:>12}{cm[2][1]:>12}{cm[2][2]:>12}')
print()
print()
print('          Precision      Recall    F1-Score')
print(f'   FIL {prec_fil:>12.4}{rec_fil:>12.4}{f1_fil:>12.4}')
print(f'   ENG {prec_eng:>12.4}{rec_eng:>12.4}{f1_eng:>12.4}')
print(f'   OTH {prec_oth:>12.4}{rec_oth:>12.4}{f1_oth:>12.4}')
print()
print(f'Weighted Avg Precision: {w_avg_prec:.4}')
print(f'Weighted Avg Recall:    {w_avg_rec:.4}')
print(f'Weighted Avg F1-Score:  {w_avg_f1:.4}')
print()

filename = 'pinoybot_decision_tree.pkl'
with open(filename, 'wb') as file:
    pickle.dump(model, file)

print("Model saved!")