import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
# we import Enum from enum to store 1, 2, 3 into strings w/o losing the values of the integers utiliized to select your options in the game.


print("")
playerchoice = input(
    "Enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n")

player = int(playerchoice)
# we convert playerchoice to an integer to utilize the conditional statements

if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.")

# sys is imported here

computerchoice = random.choice("123")
# we import random to use its operation for the computer [Python] to choose an opposing choice 

computer = int(computerchoice)
# we convert computerchoice to an integer to utilize the conditional statements

print("")
print("You chose " + str(RPS(player)).replace('RPS.', '') + ".")
# here we implement the import Enum to display the player's choice as a string instead of a number
print("Python chose " + str(RPS(computer)).replace('RPS.', '') + ".")
# here we implement the imported Enum to display Python's choice as a string instead of a number
print("")

if player == 1 and computer == 3:
    print("🎉 You win!")
elif player == 2 and computer == 1:
    print("🎉 You win!")
elif player == 3 and computer == 2:
    print("🎉 You win!")
elif player == computer:
    print("😲 Tie game!")
else:
    print("🐍 Python wins!")