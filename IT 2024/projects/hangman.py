import random
from collections import Counter

words = '''apple orange grape lemon lime pineapple dragonfruit coconut watermelon melon cherry papaya peach mango tamarind'''

words = words.split(' ')

word = random.choice(words)

if __name__ == '__main__':
    print('Guess the word! HINT: It is the name of a fruit')

    for x in word:
       print('__', end=' ')
    print()
playing = True

guess = ''
turns = len(word) + 2
correct = 0
flag = 0
try:
    while (turns !=0) and flag == 0:
        print()
        turns -=1

        try:
            play = str(input('Enter a word: '))
        except:
            print('Enter only a letter!')
            continue

        if not play.isalpha():
            print('Enter only an alphabet!')
            continue
        elif len(play)  > 1:
            print('Enter a single letter')
            continue
        elif play in guess:
            print('You have already guessed that letter')
            continue

        if play in word:
            guessed = word.count(play)
            for _ in range(guessed):
                guess += play

        for char in word:
            if char in guess and (Counter(guess) != Counter(word)):
                print(char, end=' ')
                correct += 1

            elif (Counter(guess) == Counter(word)):
                print('The word is', word, end=' ')
                flag = 1
                print('\nYou got it!')
                break
                
            else:
                print('_', end=' ')

    if turns <= 0 and (Counter(guess) != Counter(word)):
        print('Oh no! Better luck next time')
        print('The word was ',word)

except KeyboardInterrupt:
    print()
    print('You can try again.')
    exit()





