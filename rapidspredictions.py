# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("final_rapids.csv")

df = df.dropna()

df['outnumbered_within_10'] = df['teammates_within_10'] - df['opponents_within_10']
df['outnumbered_ahead_of_ball'] = df['teammates_ahead_of_ball'] - df['opponents_ahead_of_ball']
df['players_ahead_of_ball'] = df['teammates_ahead_of_ball'] + df['opponents_ahead_of_ball']

df = df.drop(['PlayerX', 'PlayerY', 'BallY','BallX','teammates_within_5','opponents_within_5','teammates_within_10','opponents_within_10', 'teammates_within_15','opponents_within_15','teammates_ahead_of_ball', 'opponents_ahead_of_ball'], axis =1)

mean_target_by_category = df.groupby('outnumbered_within_10')['IsPossGoal'].mean()
mean_target_by_category.plot(kind='bar')

mean_target_by_category = df.groupby('outnumbered_ahead_of_ball')['IsPossGoal'].mean()
mean_target_by_category.plot(kind='bar')

mean_target_by_category = df.groupby('players_ahead_of_ball')['IsPossGoal'].mean()
mean_target_by_category.plot(kind='bar')

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_curve, auc, confusion_matrix
from imblearn.over_sampling import SMOTE
import matplotlib.pyplot as plt

X = df.drop(columns=["IsPossGoal"])
y = df["IsPossGoal"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

smote = SMOTE(random_state=42)
X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)

logreg = LogisticRegression(random_state=42, max_iter=1000, penalty='l2', C=0.1, solver='liblinear')
logreg.fit(X_train_resampled, y_train_resampled)
fpr, tpr, thresholds = roc_curve(y_test, logreg.predict_proba(X_test)[:,1])
roc_auc = auc(fpr, tpr)
plt.plot(fpr, tpr, label='Logistic Regression (AUC = %0.2f)' % roc_auc)

y_pred_proba = logreg.predict_proba(X_test)[:, 1]
threshold = 0.565
y_pred = [1 if prob >= threshold else 0 for prob in y_pred_proba]

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 score:", f1)
print("Confusion Matrix:\n", conf_matrix)

plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.legend(loc="lower right")
plt.show()

