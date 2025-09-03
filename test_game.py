"""
Create a Rock Paper Scissors game with a graphical user interface (GUI) using Tkinter,
where the player selects their choice by clicking buttons and plays against a computer
that randomly selects its move. The game displays the result of each round, tracks the
scores for the player, computer, and ties, and allows the player to quit the game using a button.
"""

import random
import sys
import time
import os
from colorama import Fore, init

init(autoreset=True)
# Removed terminal clearing since this is a GUI application.

choices = ['rock', 'paper', 'scissors']
player_score = 0
computer_score = 0
tie_score = 0
rounds_played = 0

def print_slow(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def get_computer_choice():
    return random.choice(choices)

def determine_winner(player, computer):
    global player_score, computer_score, tie_score
    if player == computer:
        tie_score += 1
        return "It's a tie!"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        player_score += 1
        return "You win this round!"
    else:
        computer_score += 1
        return "Computer wins this round!"

def display_scores():
    """
    Displays the current scores for the player, computer, number of ties, and rounds played.
    Assumes that `player_score`, `computer_score`, `tie_score`, and `rounds_played` are defined in the accessible scope.
    Prints the scores in cyan color using the `Fore` module from `colorama`.
    """
    print(Fore.CYAN + f"Scores => You: {player_score} | Computer: {computer_score} | Ties: {tie_score} | Rounds Played: {rounds_played}")

# The Tkinter GUI implementation has been moved to rps_gui.py for clarity.
# This file now contains only the game logic.

if __name__ == "__main__":
    print("The Rock Paper Scissors GUI is now in rps_gui.py. Please run that file to play the game.")
