# -------------------------------------------------------------------
# 
# Excercise from: http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
#
# Objectives:
# 1. Make a two-player Rock-Paper-Scissors game. 
#
# ------------------------------------------------------------------- 

def main():
    print("*****Let's play Rock, Paper, Scissors!*****\n")

    while True:
        player1 = player_prompt(1)
        player2 = player_prompt(2)
        if winner(player1, player2) != "Replay":
            break

def player_prompt(num):
    while True:
        try:
            player = int(input("Player {}: Rock(1), Paper(2), or Scissors(3)? \n".format(num)))
            if player not in [1, 2, 3]:
                print("That is not an option. Please choose 1 (Rock), 2 (Paper), or 3 (Scissors).\n")
            else:
                return player
        except ValueError:
            print("That is not a valid answer. Please try again.\n")

def winner(player1, player2):
    if player1 == 1:
        if player2 == 1:
            print("You both played Rock. It's a tie!\n")
            return "Replay"
        elif player2 == 2:
            print("Paper covers Rock. Player 2 wins!\n")
        elif player2 == 3:
            print("Rock crushes Scissors. Player 1 wins!\n")
    elif player1 == 2:
        if player2 == 1:
            print("Paper covers Rock. Player 1 wins!\n")
        elif player2 == 2:
            print("You both played Paper. It's a tie!\n")
            return "Replay"
        elif player2 == 3:
            print("Scissors cut Paper. Player 2 wins!\n")
    elif player1 == 3:
        if player2 == 1:
            print("Rock crushes Scissors. Player 2 wins!\n")
        elif player2 == 2:
            print("Scissors cut Paper. Player 1 wins!\n")
        elif player2 == 3:
            print("You both played Scissors. It's a tie!\n")
            return "Replay"

    while True:
        answer = str(input("Would you like to play again?"))
        if answer.lower() in ["yes", "y"]:
            return "Replay"
        elif answer.lower() in ["no", "n"]:
            return "Game Complete"
        else:
            pass
    return "Game Complete"

if __name__ == "__main__":
    main()
