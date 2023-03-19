import easygui
import random

players = []

player1 = easygui.msgbox(f"Enter Player 1 username: ", "Player 1")
player2 = easygui.msgbox(f"Enter Player 2 username: ", "Player 2")

players.append([player1, 0])
players.append([player2, 0])

while True:
    for player in players:
        dice_rolls = 0
        score = 0

        while dice_rolls < 3:
            dice = []
            dice_rolls += 1

            for dice_roll in range(5):
                dice.append(random.randint(1, 6))

            dice.sort()

            if dice[0] == dice[4]:
                result = "Yahtzee!"
                score += 50

            elif dice[0] == dice[3] or dice[1] == dice[4]:
                result = "Four of a kind!"
                score += 30

            elif dice[0] == dice[2] or dice[1] == dice[3] or dice[2] \
                    == dice[4]:
                result = "Three of a kind!"
                score += 10

            else:
                result = "Better luck next time"

            roll_again = easygui.buttonbox(f"{player[0]}: dice roll "
                                           f"{dice_rolls} (Current score is "
                                           f"{score})\n\nYou rolled: "
                                           f"{str(dice).strip('[]')}\n\n"
                                           f"Choose:", "Random draw"
                                            , choices=["Roll again", "Stick"])

            if roll_again == "Stick":
                easygui.msgbox(f"{str(dice).strip('[]')}\n\n"
                               f"{result} \nScore: {score}", "Result")
            player[1] = score
            dice_rolls = 3

        else:
            player[1] = 0

    if players[0][1] == players[1][1]:
        result = f"This is a draw!\n{players[0][0]} scored {players[0][1]} " \
                 f"and {players[1][0]} also scored {players[1][1]}"

    elif players[0][1] > players[1][1]:
        result = f"The winner is {players[0][0]} with a score of " \
                 f" {players[0][1]}\n\n{players[1][0]} scored {players[1][1]}"

    else:
        result = f"The winner is {players[1][0]} with a score of " \
                 f" {players[1][1]}\n\n{players[0][0]} scored {players[0][1]}"

    play_again = easygui.buttonbox(f"{result}\n\nDo you want to play another "
                                   f"round?", "Result", choices=["Yes", "No"])

    if play_again == "Yes":
        score = 0

    else:
        break
