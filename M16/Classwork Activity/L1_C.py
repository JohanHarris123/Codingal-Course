import pandas as pd
import numpy as np
import statistics as stats

data = pd.read_csv('Titanic Dataset.csv')
print(data.head())

median_age = np.median(data['Age'])
print("Median Age of Passengers:", median_age)

median_fare = np.median(data['Fare'])
print("Median Fare of Passengers:", median_fare)

mode_age = stats.mode(data['Age'])
print("Mode Age of Passengers:", mode_age)

mode_class = stats.mode(data['Pclass'])
print("Mode Passenger Class:", mode_class)

mode_gender = data['Gender'].value_counts().index[0]
print("Mode of Feature Gender:", mode_gender)