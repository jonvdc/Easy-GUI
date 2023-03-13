import easygui
import random

cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
         "Jack", "Queen", "King", "Ace"]
suits = ["Spades", "Clubs", "Hearts", "Diamonds"]

while True:
    player = [random.choice(cards), random.choice(suits)]
    computer = [random.choice(cards), random.choice(suits)]

    if cards.index(player[0]) == cards.index(computer[0]):
        result = "This is a draw!"

    elif cards.index(player[0]) > cards.index(computer[0]):
        result = "You win!"

    else:
        result = "You lose!"

    play_again = easygui.buttonbox(f"You have the {player[0]} of {player[1]}\n"
                                   f"Computer has the {computer[0]} of "
                                   f"{computer[1]}\n\n"f"*** {result} ***\n\n"
                                   f"Do you want to play again?", "Game result",
                                   choices=["Yes", "No"])

    if play_again == "No":
        break
