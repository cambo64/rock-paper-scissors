import random

for i in range(3):


    def play_game(greeting="Hello, "):
        print(greeting + "Please select rock, paper, or scissors")
        player_move = input().lower()
        print("Your move was " + player_move)
        moves = ["rock", "paper", "scissors"]
        computer_move = random.choice(moves)
        print("Computer move is " + computer_move)

        winner = "computer"

        if player_move == computer_move:
            winner = "tie"
        elif player_move == "rock":
            if computer_move == "paper":
                winner = "computer"
            elif computer_move == "scissors":
                winner = "player"
        elif player_move == "scissors" and computer_move == "paper":
            winner = "player"
        elif player_move == "paper" and computer_move == "rock":
            winner = "player"
        elif player_move == "scissors" and computer_move == "rock":
            winner = "computer"
        elif player_move == "paper" and computer_move == "scissors":
            winner = "computer"
        else:
            print("Your move '" + player_move + "' was invalid")
            return
    
        if winner == "computer":
            input("I win, you lose. Hahahah! Shall we play again? ")
        elif winner == "tie":
            print("It's a tie...")
        else:
            input("Congratulations, you win. Can I get a rematch? ")
            if player_move == "yes":
                play_game()
            if player_move == "no": 
                print("Well, good game then.")

    play_game()





# (Parameter)