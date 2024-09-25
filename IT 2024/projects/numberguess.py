import math
import random

#ask user to input range
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

#generate random number
number = random.randint(start,end)

#to get minimum number of guesses
minimum = round(math.log(end-start+1,2))

print("You have " + f"{minimum}" + " guesses only")


#while loop
count = 0

while count <= minimum:
    count+=1

#user inputs guess number
    guess = int(input("Enter your guess: "))

#create a loop
    if guess == number:
        print(f"Congratulation! You guessed in {count} try")
        break
    elif guess < number:
        print("Try again! You guessed too low.")
    elif guess > number:
        print("Try again! You guessed too high.")

        
#to stop the loop
if count > minimum:
    print("You have used all your guesses. Better luck next time.")
    print(f"The number is {number}")