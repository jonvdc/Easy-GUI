import easygui
import random

player = 0
for roll in range(2):
    player += 1
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    easygui.msgbox(f"Player {player} you rolled \n\n{dice1} and {dice2}\n\n"
                   f"Total: {dice1 + dice2}", f"Player{player}")
