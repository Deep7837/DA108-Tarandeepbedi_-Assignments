import csv
from collections import Counter
import pandas as pd

# Path to the uploaded CSV file
file_path = "NobelLaureattes.csv"

# Lists to store country names and their respective prize counts
country_list = []
prize_count = []

# Read the CSV file line by line
with open(file_path, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip header row
    
    # Identify index of the 'Birth Country' column
    birth_country_index = header.index("Birth Country")
    
    for row in reader:
        if len(row) > birth_country_index:
            country = row[birth_country_index].strip()
            
            if country in country_list:
                index = country_list.index(country)
                prize_count[index] += 1  # Increase count for existing country
            else:
                country_list.append(country)
                prize_count.append(1)  # Add new country with count 1

# Implementing Bubble Sort to sort the lists in descending order based on prize count
n = len(prize_count)
for i in range(n - 1):
    for j in range(n - i - 1):
        if prize_count[j] < prize_count[j + 1]:
            # Swap the prize counts
            prize_count[j], prize_count[j + 1] = prize_count[j + 1], prize_count[j]
            # Swap the corresponding country names
            country_list[j], country_list[j + 1] = country_list[j + 1], country_list[j]

# Convert to DataFrame for display
df_top_20_sorted = pd.DataFrame(list(zip(country_list[:20], prize_count[:20])), 
                                columns=["Country", "Nobel Prize Count"])

# Set index to start from 1
df_top_20_sorted.index = range(1, len(df_top_20_sorted) + 1)

# Display the dataframe
a=df_top_20_sorted
print(a)