# Language Translator
import asyncio
from googletrans import Translator

# The value translator is set to import Translator
translator = Translator()


language = {"bn": "Bangla",
            "en": "English",
            "ko": "Korean",
            "fr": "French",
            "de": "German",
            "he": "Hebrew",
            "hi": "Hindi",
            "it": "Italian",
            "ja": "Japanese",
            "la": "Latin",
            "ms": "Malay",
            "ne": "Nepali",
            "ru": "Russian",
            "ar": "Arabic",
            "zh-cn": "Chinese",
            "es": "Spanish",
            "tr": "Turkish"
            }

# while True # variable to control correct language code input
def main():
    """ Your language selection loop"""

    while True:  # checking if language code is valid
        user_code = input(f"Please input desired language code. To see the language code list enter 'options' \n")

        if user_code == "options": # showing language options
            print("\nCode : Language") # Heading of language option menu
            for code, name in language.items():
                print(f"{code} => {name}") # i[0] => i[1]
            print() # adding an empty space
        elif user_code in language:
            print(f"You have selected {language[user_code]}")
            break
        else:
            print("❌ It's not a valid language code!")


    # starting translation loop
    while True:
        string = input("\nWrite the text you want to translate: \nTo exit the program write 'close'\n")

        if string == "close": # exit program command
            print(f"\nHave a nice Day!😊")
            break

        # translating method from googletrans
        translated = translator.translate(string, dest=user_code)

        # printing translation
        print(f"\n{language[user_code]} translation: {translated.text}")

        #printing pronunciation
        print(f"pronunciation: {translated.pronunciation}")

        # Print source language
        if translated.src in language:
            print(f"Translated from: {language[translated.src]}")
        else:
            print(f"Translated from: {translated.src}")

        # Save to file (optional)
        with open("translations.txt", "a", encoding="utf-8") as file:
            file.write(f"\nOriginal: {string}\n")
            file.write(f"Translated to {language[user_code]}: {translated.text}\n")
            file.write(f"Pronunciation: {translated.pronunciation}\n")
            file.write(f"Translated from: {language.get(translated.src, translated.src)}\n")
            file.write("-" * 30 + "\n")

# Run the program
main()