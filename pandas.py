import pandas as pd
import matplotlib.pyplot as plt
# Load the Iris dataset
url = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-" \
"pages/data/iris.csv"
df = pd.read_csv(url)import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.pyplot as plt 
import numpy as np
data = np.load(file=r'./data.npy')
import matplotlib.pyplot as plt 
import numpy as np

# Task i: Read the first 8 rows of the dataset
print("First 8 rows of the dataset:")
print(df.head(8))
# Task ii: Display the column names
print("\nColumn names:")
print(df.columns.tolist())
# Task iii: Fill missing data with mean value
df_filled = df.fillna(df.mean(numeric_only=True))
print("\nData after filling missing values:")
print(df_filled)
# Task iv: Remove rows with any missing values
df_cleaned = df.dropna()
print("\nData after removing rows with missing values:")
print(df_cleaned)
# Task v: Group the data by species
grouped_data = df_cleaned.groupby('species')

print("\nGrouped data by species:")
for species, group in grouped_data:
 print(f"\n{species}:")
 print(group)
# Task vi: Calculate mean, min, and max of Sepal length
print("\nStatistics for 'sepal_length':")
print(f"Mean: {df_cleaned['sepal_length'].mean():.2f}")
print(f"Min: {df_cleaned['sepal_length'].min():.2f}")
print(f"Max: {df_cleaned['sepal_length'].max():.2f}")
# Visualization example: Histogram of Sepal Length
plt.hist(df_cleaned['sepal_length'], bins=10, color='skyblue', 
edgecolor='black')
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()