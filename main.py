import random
import string

words  = ["taused","zman","dolor","sit","amet","consectetur","adipisicing","elit"]
# ,"Lorem","ipsum","dolor","sit","amet","consectetur","adipisicing","elit.","Fuga,","quibusdam","aliquam?","Autem","nisi","possimus","unde.","Quos","aut","doloribus","consequatur","dignissimos","atque","quasi","at.","Sit","autem","labore","voluptate","velit","suscipit","vero"]
def get_valid_word(words):
    word = random.choice(words)
    while '-'in word or ' ' in word:
        word = random.choice(words)
    return word

def Hangman():
    word = (get_valid_word(words).upper())
    word_letters = set(word)
    alphabit = set(string.ascii_uppercase)
    used_letters = set()
    lives = 5

    #user input

    while len(word_letters) > 0 and lives > 0:
        print(f"\n\tYou have {lives} lives left and You have used these letters: "," ".join(used_letters))

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("\n\tCurrent Words are: ",' '.join(word_list))

        user_letter = input("\n\tGuess a letter : ").upper()

        if user_letter in alphabit - used_letters:
            used_letters.add(user_letter)
        
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives-1
                print("\n\tThis letter is not in the list")
        
        elif user_letter in used_letters:
            print("\n\tYou have already used this character , Please Tray Again ")
        
        else:
            print("\n\tInvalid Character! Please Tray Again")
    if lives == 0:
        print(f"\n\tSorry! you are dead!, the word was {word}")
    else:
        print(f"\n\tWow! You guessed the world {word} !!")

while True:
    x = input("\n\tHangman Game Python CLI \
        \n\t[1]::: play Game \
        \n\t[2]::: Exit\n\t")
    if x == '1':
        Hangman()
    else:
        exit()

