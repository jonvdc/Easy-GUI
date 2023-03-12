import easygui
import random

while True:
    weapons = ["Paper", "Scissors", "Rock"]
    computer = random.choice(weapons)
    play_again = easygui.buttonbox("Welcome to Rock, Paper, Scissors\n\n"
                                   "Rock beats Scissors\n"
                                   "Scissors beats Paper\n"
                                   "Paper beats Rock\n"
                                   "Do you want to play?\n"
                                   "Welcome and Rules", choices=["Yes", "No"])
    if play_again == "No":
        break
    else:
        player = easygui.buttonbox("Choose your weapon", "Choose weapon",
                                   choices=[weapons[0], weapons[1],
                                            weapons[2]])
        easygui.msgbox(f"You chose {player} and the computer "
                       f"chose {computer}", "Choice")

        if computer == player:
            result = "That was a draw"
        elif computer == "Paper" and player == "Rock" or computer == "Scissors":
            result = "Sorry, that was a loss"
        else:
            result = "Congratulations, you win!"

        easygui.msgbox(f"{result}")
print("Goodbye")
