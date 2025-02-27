import unicodedata
import collections

# Function to detect script of a given character
def detect_script(text):
    scripts = collections.Counter()
    for char in text:
        if char.isalpha():
            script = unicodedata.name(char).split()[0]
            scripts[script] += 1
    return scripts

# Load the language detection file
file_path = "Data_for_language_detection.txt"

with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

# Dictionary to count words per script
script_word_count = collections.Counter()
# Set to track unique languages
unique_languages = set()

def count_words_in_scripts():
    for line in lines:
        parts = line.split("=")
        if len(parts) > 1:
            language = parts[0].strip()
            words = parts[-1].strip()  # Extracting the translated part
            unique_languages.add(language)
            script_counts = detect_script(words)
            for script, count in script_counts.items():
                script_word_count[script] += count

# Run the word count function
count_words_in_scripts()

# Print the summary
print("Summary of different language scripts present:")
for script, count in script_word_count.items():
    print(f"{script}: {count} words")

# Print the total number of languages detected
print(f"Total number of languages detected: {len(unique_languages)}")