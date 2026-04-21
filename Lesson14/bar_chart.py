import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('avgIQpercountry.csv')

# Filter the DataFrame to include only rows where 'Average IQ' is greater than or equal to 100
filtered_df = df[df["Average IQ"] >= 100]

# Sort the filtered DataFrame by 'Average IQ' in descending order
filtered_df = filtered_df.sort_values(by="Average IQ", ascending=False)

# Print the filtered and sorted DataFrame to verify the data
print(filtered_df)

# Create a figure for the bar chart with a specified size
plt.figure(figsize=(14, 8))

# Create a bar chart with 'Country' on the x-axis and 'Average IQ' on the y-axis
bars = plt.bar(filtered_df["Country"], filtered_df["Average IQ"], color="skyblue")

# Add a title to the chart
plt.title("Average IQ by Country (IQ >= 100)", fontsize=16)

# Add labels to the x-axis and y-axis
plt.xlabel("Country", fontsize=14)
plt.ylabel("Average IQ", fontsize=14)

# Rotate the x-axis labels for better readability
plt.xticks(rotation=90, fontsize=10)
plt.yticks(fontsize=10)

# Add gridlines to the y-axis for better readability
plt.grid(axis='y', linestyle='--', alpha=0.8)

# Add text labels on the bars
plt.bar_label(bars, fmt='%.2f', fontsize=10, color='black')

# Adjust the layout to ensure everything fits without overlapping
plt.tight_layout()

# Display the bar chart
plt.show()