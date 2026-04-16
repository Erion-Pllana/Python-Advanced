# Importing necessary libraries
from matplotlib import pyplot as plt
import pandas as pd

# Reading the dataset
df = pd.read_csv('avgIQpercountry.csv')

# Calculating average IQ by continent
avg_iq_by_continent = df.groupby('Continent')['Average IQ'].mean()

# Creating a new figure for the plot
plt.figure(figsize=(10, 6))

# Plotting the average IQ by continent as a line plot with markers
avg_iq_by_continent.plot(kind='line', marker='o', color='skyblue')

# Adding title and labels
plt.title('Average IQ by Continent')
plt.xlabel('Continent')
plt.ylabel('Average IQ')

# Adding grid lines for both axes
plt.grid(axis='both', linestyle='--', alpha=0.7)

# Displaying the plot
plt.show()