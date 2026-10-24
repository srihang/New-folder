#This is a rock paper scissors bot and it enables you to play a game of rock paper scissors with the system. 
#The system will direct you to choose out of the 3 options and the computer will choose one as well
#If both of you choose the same option it will end up being a draw
#The computer choice is randomly generated
#Then ur choice and the computers choice are compared and a winner is decided
#To play again you can just find 

import random 

print("Welcome to Rock Paper Scissors!\n")and 

choices = ["Rock", "Paper", "Scissors"]

while True:
    print("Choose an option")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")

    user_input = int(input("Enter your choice (1-3): "))
    user_choice = choices[user_input - 1]

    computer_choice = random.choice(choices)

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}") 

    if user_choice == computer_choice:
        print("It is a tie. Play again!")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or 
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper") 
    ):
        print("You Win :) !!!")
    else:
        print("You Lose :( !!!")
    
    play_again = input("\nPlay again? y/n")
    if play_again != "y":
        break
    
    print()
    
