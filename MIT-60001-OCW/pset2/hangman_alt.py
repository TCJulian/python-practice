'''
Problem Set 2, hangman.py
'''

# Hangman Game
# -----------------------------------
# Helper code

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    guessed_word = ""
    for letter in secret_word:
        if letter not in letters_guessed:
            guessed_word += "_ "
        else:
            guessed_word += letter
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    remaining_letters = ""
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            remaining_letters += letter
    return remaining_letters


def calculate_total_score(secret_word, guesses):
    '''
    secret_word: string, the word the user is guessing
    guesses: the total number of guesses the user has left in the current game
    returns: an int that represents the total score for the game. This is calulated
        using the the number of guesses remaining times the number of unique
        characters in the secret word.
    '''
    unique_letters = ""
    for letter in secret_word:
        if letter not in unique_letters:
            unique_letters += letter
    return guesses * len(unique_letters)


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = []
    guesses = 6
    warnings = 3

    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print("You have 3 warnings left.")

    while guesses > 0:
        print("----------")
        print(f"You have {guesses} guess(es) left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        guessed_letter = input("Please guess a letter: ")

        if not guessed_letter.isalpha():
            if warnings > 0:
                warnings -= 1
                print(
                    "Oops! That is not a valid letter. "
                    f"You have {warnings} warnings left: "
                    f"{get_guessed_word(secret_word, letters_guessed)}")
            else:
                guesses -= 1
                print(
                    "Oops! That is not a valid letter. "
                    "You have no warnings left, so you lose one guess: "
                    f"{get_guessed_word(secret_word, letters_guessed)}")
            continue

        guessed_letter = guessed_letter.lower()

        if guessed_letter in letters_guessed:
            if warnings > 0:
                warnings -= 1
                print(
                    "Oops! You have already guessed that letter. "
                    f"You have {warnings} warnings left: "
                    f"{get_guessed_word(secret_word, letters_guessed)}")
            else:
                guesses -= 1
                print(
                    "Oops! You have already guessed that letter. "
                    "You have no warnings left, so you lose one guess: "
                    f"{get_guessed_word(secret_word, letters_guessed)}")
            continue

        letters_guessed.append(guessed_letter.lower())

        if guessed_letter in secret_word:
            print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
        else:
            print(
                "Oops! That letter is not in my word: "
                f"{get_guessed_word(secret_word, letters_guessed)}")
            if guessed_letter in "bcdfghjklmnpqrstvwxyz":
                guesses -= 1
            elif guessed_letter in "aeiou":
                guesses -=2

        if is_word_guessed(secret_word, letters_guessed):
            break

    if guesses <= 0:
        print("----------")
        print(f"Sorry, you ran out of guesses! The secret word was: {secret_word}")
    else:
        print("----------")
        print("Congratulations, you won!")
        print(f"Your total score for this game is: {calculate_total_score(secret_word, guesses)}")



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    my_word = my_word.replace(' ', '')
    if len(my_word) != len(other_word):
        return False

    for position, letter in enumerate(my_word):
        secret_letter = other_word[position]
        if secret_letter == letter or (letter == '_' and secret_letter not in my_word):
            continue
        else:
            return False
    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_matches = []

    for word in wordlist:
        if match_with_gaps(my_word, word):
            possible_matches.append(word)

    if len(possible_matches) > 0:
        for match in possible_matches:
            print(match, end=" ")
        print("")
    else:
        print("No matches found")


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    letters_guessed = []
    guesses = 6
    warnings = 3

    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print("You have 3 warnings left.")

    while guesses > 0:
        print("----------")
        print(f"You have {guesses} guess(es) left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        guessed_letter = input("Please guess a letter: ")

        if guessed_letter == "*":
            print("Possible word matches are:")
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
            continue

        if not guessed_letter.isalpha():
            if warnings > 0:
                warnings -= 1
                print(
                    "Oops! That is not a valid letter. "
                    f"You have {warnings} warnings left: "
                    f"{get_guessed_word(secret_word, letters_guessed)}")
            else:
                guesses -= 1
                print(
                    "Oops! That is not a valid letter. "
                    "You have no warnings left, so you lose one guess: "
                    f"{get_guessed_word(secret_word, letters_guessed)}")
            continue

        guessed_letter = guessed_letter.lower()

        if guessed_letter in letters_guessed:
            if warnings > 0:
                warnings -= 1
                print(
                    "Oops! You have already guessed that letter. "
                    f"You have {warnings} warnings left: "
                    f"{get_guessed_word(secret_word, letters_guessed)}")
            else:
                guesses -= 1
                print(
                    "Oops! You have already guessed that letter. "
                    "You have no warnings left, so you lose one guess: "
                    f"{get_guessed_word(secret_word, letters_guessed)}")
            continue

        letters_guessed.append(guessed_letter.lower())

        if guessed_letter in secret_word:
            print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
        else:
            print(
                "Oops! That letter is not in my word: "
                f"{get_guessed_word(secret_word, letters_guessed)}")
            if guessed_letter in "bcdfghjklmnpqrstvwxyz":
                guesses -= 1
            elif guessed_letter in "aeiou":
                guesses -=2

        if is_word_guessed(secret_word, letters_guessed):
            break

    if guesses <= 0:
        print("----------")
        print(f"Sorry, you ran out of guesses! The secret word was: {secret_word}")
    else:
        print("----------")
        print("Congratulations, you won!")
        print(f"Your total score for this game is: {calculate_total_score(secret_word, guesses)}")



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
