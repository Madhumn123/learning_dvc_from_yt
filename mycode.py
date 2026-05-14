import pandas as pd
import os

# Create initial DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Add new rows
df.loc[len(df)] = {'Name': 'GF1', 'Age': 20, 'City': 'City1'}
df.loc[len(df)] = {'Name': 'GF2', 'Age': 30, 'City': 'City2'}

# Create data directory
data_dir = 'data'
os.makedirs(data_dir, exist_ok=True)

# File path
file_path = os.path.join(data_dir, 'sample_data.csv')

# Save CSV
df.to_csv(file_path, index=False)

print(f"CSV file saved to {file_path}")