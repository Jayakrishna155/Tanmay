import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Create a new column 'Day' to extract the day from the date
df['Day'] = df['Date'].dt.day

# Filter the DataFrame to include only the relevant columns
df = df[['Date', 'Time', 'Volume', 'Day']]

# Define a function to calculate rank based on volume
def calculate_rank(row):
    current_date = row['Date']
    current_time = row['Time']
    current_volume = row['Volume']
    
    # Filter data for the last 5 days including the current day
    relevant_data = df[(df['Date'] >= current_date - pd.DateOffset(days=4)) & (df['Date'] <= current_date)]
    
    # Filter data for the specific time across days
    relevant_data = relevant_data[relevant_data['Time'] == current_time]
    
    # Calculate rank based on volume
    rank = (relevant_data['Volume'] > current_volume).sum() + 1
    
    return rank

# Apply the function to each row to calculate rank and store it in a new column 'Rank'
df['Rank'] = df.apply(calculate_rank, axis=1)

# Display the DataFrame with the 'Rank' column
print(df.head())
