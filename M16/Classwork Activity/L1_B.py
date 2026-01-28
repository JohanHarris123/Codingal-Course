import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Titanic Dataset.csv')
print(data.head())

mean_fare_by_class = data['Fare'].mean()
print("Mean Fare by Class:\n", mean_fare_by_class)

plt.figure(figsize=(6,4))
plt.hist(data['Fare'], bins=30, color='skyblue', edgecolor='black')
plt.title("Distribution of Passenger Fares")
plt.xlabel("Fare")
plt.ylabel("Number of Passengers")
plt.show()