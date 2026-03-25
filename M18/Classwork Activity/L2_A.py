import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = sns.load_dataset('titanic')

print(data.head())
print(data.info())
print(data.isnull().sum())

#Data Visualization (Seaborn)
sns.countplot(x='survived', data=data)
plt.title("Survival Count (0 -> Dead, 1 -> Survived)")
plt.show()

sns.countplot(x='sex', hue='survived', data=data)
plt.title("Survival based on Gender")
plt.show()

sns.countplot(x='pclass', hue='survived', data=data)
plt.title("Survival based on passenger class")
plt.show()

sns.histplot(data['age'].dropna(), kde=True)
plt.title("Age Distribution")
plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(data.corr(numeric_only=True), annot=True,)
plt.title("Correlation Heatmap")
plt.show()

#Data Preprocessing
data['age'].fillna(data['age'].mean(), inplace=True)
data['embarked'].fillna(data['embarked'].mode()[0], inplace=True)

data.drop(['deck', 'alive', 'class', 'who', 'adult_male', 'embark_town'], axis=1, inplace=True)

data = pd.get_dummies(data, drop_first=True)
print(data.head())

#Train AI Model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

x = data.drop('survived', axis=1)
y = data['survived']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

model = LogisticRegression(max_iter=1000)

model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print("Accuracy: ", accuracy_score(y_test, y_pred))

sample = x.iloc[0:1]
prediction = model.predict(sample)
print("Prediction: ", prediction)
if prediction[0] == 1:
    print("Passenger would survied")
else:
    print("Passenger would not survive")