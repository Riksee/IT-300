import random

print("NOTE: \n"
      +"Rock beats Scissors \n"
      +"Scissors beats Paper \n"
      +"Paper beats Rock.")
while True:

    print("Pick your play \n 1(Rock) \n 2(Paper) \n 3(Scissors)")
 
 #User plays
    print("PLAYER")
    play = int(input("Enter your play: "))

    while play > 3 or play < 1:
        play = int(input("Play a valid option: "))

    if play == 1:
        choice = "Rock"
    elif play == 2:
        choice = "Paper"
    else:
        choice = "Scissors"


    print("You played", choice)

    #computer plays
    print("COMPUTER")

    comp_play = random.randint(1, 3)

    while comp_play == play:
        comp_play = random.randint(1, 3)

    if comp_play == 1:
        comp_choice = "Rock"
    elif comp_play == 2:
        comp_choice = "Paper"
    else:
        comp_choice = "Scissors"
    print("Computer played", comp_choice)

    #result if play is the same
    if play == comp_play:
        print("It's a Draw", end="")
        result = "Draw"

    #result if rock and scissors are played
    if (play == 1 and comp_play == 3):
        print("Rock Wins")
        result = "Rock"
    elif (play == 3 and comp_play ==1):
        print("Rock Wins")
        result = "Rock"

    #result if paper and scissors are played
    if (play == 2 and comp_play == 3):
        print("Scissors Wins")
        result = "Scissors"
    elif (play == 3 and comp_play ==2):
        print("Scissors Wins")
        result = "Scissors"

    #result if rock and paper are played
    if (play == 1 and comp_play == 2):
        print("Paper Wins")
        result = "Paper"
    elif (play == 2 and comp_play ==1):
        print("Paper Wins")
        result = "Paper"


    if result == "Draw":
        print("It's a Draw")
    if result == choice:
        print("Player Wins!")
    else:
        print("Computer Wins! \n Better Luck Next Time.")

    print("Do you want to play again?(Y/N)")
    ans = input().lower()
    if ans == "n":
        break

print("See you next time!")  

