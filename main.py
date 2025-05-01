import random

VALID_MOVES = {"R": "Rock", "P": "Paper", "S": "Scissors"}


def get_player_move():
    while True:
        move = input("Choose [R]ock, [P]aper, or [S]cissors: ").upper()
        if move in VALID_MOVES:
            return move
        print("Invalid choice. Please enter R, P, or S.")


def get_computer_move():
    return random.choice(list(VALID_MOVES.keys()))


def determine_winner(player_move, computer_move):
    if player_move == computer_move:
        return "tie"
    wins = {
        "R": "S",  # Rock beats Scissors
        "P": "R",  # Paper beats Rock
        "S": "P",  # Scissors beats Paper
    }
    return "player" if wins[player_move] == computer_move else "computer"


def play_game():
    print("Welcome to Rock, Paper, Scissors! 🪨📃✂️")
    player_score = 0
    computer_score = 0

    while True:
        player_move = get_player_move()
        computer_move = get_computer_move()

        print(f"You chose {VALID_MOVES[player_move]}")
        print(f"Computer chose {VALID_MOVES[computer_move]}")

        result = determine_winner(player_move, computer_move)

        if result == "tie":
            print("It's a tie!")
        elif result == "player":
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score | You: {player_score} | Computer: {computer_score} |")

        again = input("Play again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    play_game()
