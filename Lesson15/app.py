import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('weather_tokyo_data.csv')

filtered_df = df[df["weather_tokyo_data.csv"] >= 100]

plt.figure(figsize=(12, 6))
plt.plot( df["Date"], ["Temperature"])
plt.title('Temperature Trends')
plt.xlabel('Date')
plt.ylabel('Temperature ( C)')
plt.grid(True)
plt.tight_layout()
plt.show()