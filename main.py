from words import words
import random

def get_valid_word(words): 
    word =  random.choice(words)
    while '-' in word or ' ' in word:
        word =  random.choice(words)
    return word.upper()    

def hangman():
    special_characteres_and_numbers = ["`", "~", "!", "¡", "@", "²", "#", "³", "$", "¤", "%", "€", "^", "¼", "&", "½", "*", "¾", "(", "‘", ")", "’", "_", "-", "¥", "=", "+", "×", "[", "{", "«", "]", "}", "»", "|", "¬", ";", ":", "¶", "'", "´", ",", "<", "ç", ".", ">", "/", "?", "¿", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    lives = 0
    word = get_valid_word(words)
    # print("_ " * len(word))
    print("You have 6 lives")

    letter = input("Choose a letter: ").upper()

    if letter in special_characteres_and_numbers:
        print("\nPorfavor, digite una letra valida. \n")
        hangman()
    else:
        if len(letter) > 1:
            print("\nPorfavor, solo digite una letra, no mas. \n")
            hangman()
        else:
            print("Todo bien.")
hangman()
# print(get_valid_word(words))