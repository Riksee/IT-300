import random

#ask user to input name
user = input("Enter your name: ")

#declare maximum number of guesses
maximum = 6

#create an array of words
words = ["apple","count","later","python","guess","word"]

#select a random word from array
word = random.choice(words)

print("Hello, " + user + "! Guess an alphabet")
print(f"You have {maximum} guesses")

alphabets = ''

while maximum > 0:
    fails = 0

    for x in word:

        if x in alphabets:
            print(x, end="")

        else:
            print("...")

            fails+=1

    if fails == 0:
        print("\nYou guessed right!")
        print("The word is",word)
        break

    print()
    guess = input("Guess an alphabet:")

    alphabets += guess

    if guess not in word:
        maximum -= 1
        print("Wrong")

        print(f"You have {maximum} more guesses.")

        if maximum == 0:
            print("You guessed wrong, try again!")

