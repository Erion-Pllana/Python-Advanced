import pandas as pd
import matplotlib.pyplot as plt

# 1. LOAD THE DATA
# Ensure 'weather_tokyo_data.csv' is in your project folder
file_path = 'weather_tokyo_data.csv'
df = pd.read_csv(file_path)

# PREPROCESSING
df.columns = df.columns.str.strip()

def clean_temp(val):
    if isinstance(val, str):
        val = val.strip()
        if val.startswith('(') and val.endswith(')'):
            return -float(val[1:-1])
        return float(val)
    return float(val)

df['temperature'] = df['temperature'].apply(clean_temp)
df['day'] = df['day'].astype(str).str.strip()
df['date'] = pd.to_datetime(df['year'].astype(str) + '/' + df['day'])

# --- TASK 1: TEMPERATURE OVERVIEW ---
avg_temp = df['temperature'].mean()
print(f"1. Overall Average Temperature: {avg_temp:.2f}°C")

# --- TASK 2: MONTHLY TEMPERATURE ---
monthly_avg = df.groupby(df['date'].dt.month)['temperature'].mean()

plt.figure(figsize=(10, 5))
monthly_avg.plot(kind='bar', color='skyblue')
plt.title('Monthly Average Temperature')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=0)
plt.savefig('monthly_avg_temp.png')
print("\n2. Monthly bar plot saved.")

# --- TASK 3: HIGHS AND LOWS ---
hottest_row = df.loc[df['temperature'].idxmax()]
coldest_row = df.loc[df['temperature'].idxmin()]

print("\n3. Hottest Day (Entire Row):")
print(hottest_row.to_frame().T)
print("\n3. Coldest Day (Entire Row):")
print(coldest_row.to_frame().T)

# --- TASK 4a: TEMPERATURE TRENDS (LINE GRAPH OVER TIME) ---
plt.figure(figsize=(12, 6))
plt.plot(df['date'], df['temperature'], color='orange', linewidth=1)
plt.title('Temperature Trends Over Time')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig('temp_trend.png')
print("\n4a. Temperature trend line graph saved.")

# --- TASK 4b: SEASONAL AVERAGE (LINE GRAPH) ---
def get_season(month):
    if month in [12, 1, 2]: return 'Winter'
    elif month in [3, 4, 5]: return 'Spring'
    elif month in [6, 7, 8]: return 'Summer'
    else: return 'Autumn'

df['season'] = df['date'].dt.month.apply(get_season)

# Sorting seasons logically for a better looking line
season_order = ['Winter', 'Spring', 'Summer', 'Autumn']
seasonal_avg = df.groupby('season')['temperature'].mean().reindex(season_order)

print("\n4b. Seasonal Average Temperatures:")
print(seasonal_avg)

# Visualization: Seasonal Line Graph
plt.figure(figsize=(8, 5))
plt.plot(seasonal_avg.index, seasonal_avg.values, marker='o', linestyle='-', color='green', linewidth=2)
plt.title('Average Temperature by Season (Line Graph)')
plt.xlabel('Season')
plt.ylabel('Temperature (°C)')
plt.grid(True, linestyle=':', alpha=0.7)
plt.savefig('seasonal_avg_line.png')
print("4b. Seasonal line plot saved as 'seasonal_avg_line.png'")

# Show all plots
plt.show()