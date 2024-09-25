import random

code = random.randrange(100, 1000)

code_break = int(input("Guess the 3 digit number:"))

if(code_break == code):
    print("You guessed it in one try! You are a MasterMind")
else:
    counter = 0


    while(code_break != code):
        counter += 1

        count = 0

        code_break = str(code_break)
        code = str(code)
        correct = ['?']*3

        for x in range(0, 3):
            
            if (code_break[x] == code[x]):
                count +=1
                correct[x] = code_break[x]
            else:
                continue
        if (count < 3) and (count != 0):

            print('Almost there! You got',count, 'right!')
            print('These numbers were correct')

            for y in correct:
                print(y, end=' ')
            print('\n')
            code_break = int(input('Enter your next choice: '))

        
        elif (count == 0):
            print("None of the numbers match")
            code_break = int(input('Enter your next choice: '))

    if code_break == code:
        counter += 1
        print('You are a MasterMind!')
        print("You used", counter, 'tries')
