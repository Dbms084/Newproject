from random import randint

moves = ["rock", "paper", "scissors"]
running = True

while running:
    try:
        player = int(input("Enter 0: Rock, 1: Paper, and 2: Scissors! \n "))
        
        if player > 2 or player < 0:
            print("Invalid input. Please enter a number in the range 0-2!\n")
        else:
            computer = moves[randint(0, 2)]
            player_choice = moves[player]
            print(f"User's choice is {player_choice} and computer's choice is {computer}!\n")
            if player_choice == computer:
                print("It's a tie!\n")
            elif player_choice == "rock":
                if computer == "paper":
                    print("You lose",computer,"beats",player_choice)
                else:
                    print("You win!",player,"beats",computer)
            elif player_choice == "paper":
                if computer == "scissors":
                    print("You lose!",computer,"beats",player_choice)
                else:
                    print("You win!",player_choice,"beats",computer)
            elif player_choice == "scissors":
                if computer == "rock":
                    print("You lose!",computer,"beats",player_choice)
                else:
                    print("You win!",player_choice,"beats",computer)
            else :
                print(f"You lose!",computer,"beats",player_choice) 

            play_again = input("Would you like to play again? (y/n): ").lower()
            if play_again != "y":
                running = False    
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")
print("Thanks for playing!")                  