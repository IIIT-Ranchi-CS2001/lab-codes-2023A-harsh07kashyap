import pandas as pd
import numpy as np

file_path = r"C:\Users\hp\Downloads\AQI_Data.csv"

data = pd.read_csv(file_path)
print("File loaded successfully")
# print(data.head())

# Display the first five rows
print("First five rows of the dataset are:")
print(data.head())

# Display the last six rows
print("Last six rows of the dataset are:")
print(data.tail(6))

# Summary statistics
print("Summary statistics : ")
print(data.describe())

# Aqi mean
# print("AQI mean of the cities are:")
# a=data['AQI'].mean()
# print(a)

a=data.groupby("City")['AQI'].apply(np.mean)
print(a)
b=data.groupby("City")['PM2.5'].apply(np.mean)
print(b)
c=data.groupby("City")['PM10'].apply(np.mean)
print(c)


missing_values = data.isnull().sum()
print("Missing values in each column:")
print(missing_values)

numeric_columns = data.select_dtypes(include=[np.number]).columns
data[numeric_columns] = data[numeric_columns].apply(lambda col: col.fillna(col.mean()), axis=0)

updated_missing_values = data.isnull().sum()
print("\nMissing values after replacement:")
print(updated_missing_values)

print("\nUpdated dataset (first five rows):")
print(data.head())



aqi_array = data['AQI'].to_numpy()

aqi_mean = np.mean(aqi_array)
aqi_median = np.median(aqi_array)
aqi_std = np.std(aqi_array)

print(f"AQI Mean: {aqi_mean}")
print(f"AQI Median: {aqi_median}")
print(f"AQI Standard Deviation: {aqi_std}")
