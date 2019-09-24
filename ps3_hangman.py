import string
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    wordChecker = 0
    for i in secretWord:
        if i in lettersGuessed:
            wordChecker += 1
    if wordChecker == len(secretWord):
        return True
    else:
        return False


def getGuessedWord(secretWord, lettersGuessed):
    underWord = secretWord
    for i in secretWord:
        if i not in lettersGuessed:
            underWord = underWord.replace(i,"_ ")
    return underWord


def getAvailableLetters(lettersGuessed):
    availableLetters = string.ascii_lowercase
    for i in availableLetters:
        if i in lettersGuessed:
            availableLetters = availableLetters.replace(i,'')
    return availableLetters


def hangman(secretWord):
    lettersGuessed = []
    numberOfGuesses = 8
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is " + str(len(secretWord)) + " letters long.")
    print("------------")
    while numberOfGuesses >= 1 and (isWordGuessed(secretWord,lettersGuessed)) == False:
        print("You have " + str(numberOfGuesses) + " guesses left.")
        print("Available Letters: " + getAvailableLetters(lettersGuessed))
        guess = input("Please guess a letter: ")
        guess = str(guess.lower())
        if guess in secretWord and guess not in lettersGuessed:
            lettersGuessed.append(guess)
            print("Good guess: " + str(getGuessedWord(secretWord,lettersGuessed)))
            print("------------")
        elif guess not in secretWord and guess not in lettersGuessed:
            numberOfGuesses -= 1
            lettersGuessed.append(guess)
            print("Oops! That letter is not in my word: " + str(getGuessedWord(secretWord,lettersGuessed)))
            print("------------")
        elif guess in lettersGuessed:
            print("Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord,lettersGuessed)))
            print("------------")
    if numberOfGuesses <= 1:
        print("Sorry, you ran out of guesses. The word was " + secretWord + '.')
        return
    elif isWordGuessed(secretWord, lettersGuessed):
        print("Congratulations, you won!")
        return
    return


wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
