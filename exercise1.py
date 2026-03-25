import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

df = sns.load_dataset('titanic')

print("First 5 rows")
print(df.head())

print("Dataset Info:")
print(df.info())

df = df.drop(['deck', 'embark_town', 'alive', 'class', 'who', 'adult_male'], axis=1)