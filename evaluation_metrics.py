from sklearn.metrics import *
import joblib
import pandas as pd

df = pd.read_csv('/home/luhita/Desktop/project/articles/large.csv')

features = list(df.columns)
features.remove('class')
X = df[features]
y = df['class']

model = joblib.load('/home/luhita/Desktop/project/articles/model_rf1.joblib')

print(f"Class 0: {len(df[df['class']==0])}")
print(f"Class 1: {len(df[df['class']==1])}")

print(f"Accuracy: {accuracy_score(y, model.predict(X))}")
print(f"Confusion Matrix:\n {confusion_matrix(y, model.predict(X))}")
print(f"Precision: {precision_score(y,model.predict(X))}")
print(f"Recall: {recall_score(y,model.predict(X))}")
print(f"F1 score: {f1_score(y,model.predict(X))}")