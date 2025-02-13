import os
import requests
import csv
import re

# Step 1: Define the Correct CSV file URL and Paths
csv_url = "https://raw.githubusercontent.com/prasertcbs/basic-dataset/master/Country_Flags.csv"
csv_filename = "Country_Flags.csv"
flags_dir = "flags"

# Step 2: Download and Save the CSV File
response = requests.get(csv_url)
if response.status_code == 200:
    with open(csv_filename, "wb") as file:
        
        file.write(response.content)
    print(f"CSV file '{csv_filename}' downloaded successfully.")
else:
    print("Failed to download CSV file.")
    exit()

# Step 3: Create 'flags' Directory if Not Exists
os.makedirs(flags_dir, exist_ok=True)

# Step 4: Read CSV File and Extract Image URLs
with open(csv_filename, newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)

    # Print actual column names for debugging
    print("Column Names in CSV:", reader.fieldnames)

    # Strip BOM and normalize column names
    reader.fieldnames = [name.lstrip("\ufeff").strip() for name in reader.fieldnames]

    for row in reader:
        country = row.get("Country", "").strip()
        image_url = row.get("ImageURL", "").strip()

        if not country or not image_url:
            print(f"Skipping row with missing data: {row}")
            continue  # Skip rows with missing values

        # Replace special characters for safe filenames
        country_clean = re.sub(r'[^\w\s-]', '', country).replace(" ", "_")

        # Define image file path
        image_filename = os.path.join(flags_dir, f"{country_clean}.png")

        # Download and Save the Flag Image
        img_response = requests.get(image_url)
        if img_response.status_code == 200:
            with open(image_filename, "wb") as img_file:
                img_file.write(img_response.content)
            print(f"Downloaded {country}'s flag.")
        else:
            print(f"Failed to download {country}'s flag from {image_url}.")

print("All flags downloaded successfully!")
