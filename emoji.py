import random

# Step 1: Basic Emoji Translator
def translate_to_emojis(sentence):
    emoji_dict = {
        "hello": "\U0001F44B",
        "world": "\U0001F30E",
        "love": "\U00002764",
        "happy": "\U0001F60A",
        "sad": "\U0001F622",
        "cat": "\U0001F431",
        "dog": "\U0001F436",
        "food": "\U0001F354",
        "party": "\U0001F389",
        "sun": "\U0001F31E",
        "friend": "\U0001F9D1\U0000200D\U0001F91D\U0000200D\U0001F9D1",
        "music": "\U0001F3B6",
        "computer": "\U0001F4BB",
        "phone": "\U0001F4F1",
        "book": "\U0001F4D6",
        "coffee": "\U00002615",
        "car": "\U0001F697",
        "plane": "\U00002708",
        "beach": "\U0001F3D6",
        "rain": "\U0001F327"
    }
    words = sentence.lower().split()
    translated = [emoji_dict.get(word, word) for word in words]
    return ' '.join(translated)

# Step 2: Mood-Based Auto-Filling Emoji Generator
def mood_fill(sentence, mood):
    mood_emojis = {
        "happy": ["\U0001F603", "\U0001F389", "\U0001F973", "\U0001F60A", "\U0001F31E"],
        "sad": ["\U0001F622", "\U0001F494", "\U0001F62D", "\U0001F327", "\U0001F61E"],
        "excited": ["\U0001F929", "\U0001F386", "\U0001F389", "\U0001F525", "\U0001F4A5"],
        "angry": ["\U0001F621", "\U0001F92C", "\U0001F4A5", "\U0001F620", "\U0001F624"],
        "relaxed": ["\U0001F60C", "\U0001F3D4", "\U0001F6CC", "\U0001F3B6", "\U0001F379"]
    }
    if mood in mood_emojis:
        sentence += ' ' + ' '.join(random.sample(mood_emojis[mood], 3))
    return sentence

# Step 3: Integrate features
def main():
    while True:
        user_input = input("What would you like to do?\n1: Translate to emoji\n2: Add mood-based emojis\nType 'exit' to quit: ")
        if user_input.lower() == 'exit':
            break

        if user_input == '1':
            sentence = input("Enter a sentence to translate into emojis: ")
            translated_sentence = translate_to_emojis(sentence)
            print(f"Translated Sentence: {translated_sentence}\n")

        elif user_input == '2':
            sentence = input("Enter a sentence to add mood-based emojis: ").lower()
            if "fill with happy emoji" in sentence:
                mood_type = "happy"
            elif "fill with sad emoji" in sentence:
                mood_type = "sad"
            elif "fill with excited emoji" in sentence:
                mood_type = "excited"
            elif "fill with angry emoji" in sentence:
                mood_type = "angry"
            elif "fill with relaxed emoji" in sentence:
                mood_type = "relaxed"
            else:
                mood_type = input("Enter the mood (happy, sad, excited, angry, relaxed): ").lower()

            cleaned_sentence = sentence.split("(fill with ")[0].strip()
            mood_filled_sentence = mood_fill(cleaned_sentence, mood_type)
            print(f"Mood-Filled Sentence: {mood_filled_sentence}\n")

        else:
            print("Invalid option. Please choose 1 or 2.\n")

if __name__ == "__main__":
    main()