"""ROCK, PAPER AND SCISSOR GAME"""

import random
import colorama
from colorama import Fore, Back, Style

game = Fore.BLUE + "RPS\033[39m"
name = input("Enter your name: ")
print(f"Hello {name} welcome to {game}")
print("You play against the PC for 10 rounds, the one who won the most, win the game!")
options = ["rock", "paper", "scissor"]
user_win = 0
compute_win = 0
initial_round = 1
max_round = 10

while initial_round <= max_round:
    pc = random.choice(options)
    print(f"Numbers of rounds: {initial_round}")
    print(Style.BRIGHT + "Enter r for rock, p for paper and s for scissor\033[39m")
    user = input("Enter here: ")
    if pc == "rock":
        if user == "p":
            print(Fore.GREEN + "Computer : rock")
            print(Fore.BLUE + "you win this round\033[39m")
            user_win += 1
            print(f"\033[39mYour score: {user_win}")
            print(f"\033[39mcomputer score: {compute_win}\033[39m")
        elif user == "s":
            print(Fore.GREEN + "Computer : rock")
            print(Fore.RED + "you lost this round")
            compute_win += 1
            print(f"\033[39mYour score: {user_win}")
            print(f"\033[39mcomputer score: {compute_win}\033[39m")
        elif user == "r":
            print(Fore.GREEN + "Computer : rock")
            print("\033[39mIts a tie")
        else:
            print("Invalid input")
        initial_round += 1


    elif pc == "paper":
        if user == "s":
            print(Fore.GREEN + "Computer : paper")
            print(Fore.BLUE + "you win this round\033[39m")
            user_win += 1
            print(f"\033[39mYour score: {user_win}")
            print(f"\033[39mcomputer score: {compute_win}\033[39m")
        elif user == "r":
            print(Fore.GREEN + "Computer : paper")
            print(Fore.RED + "you lost this round")
            compute_win += 1
            print(f"\033[39mYour score: {user_win}")
            print(f"\033[39mcomputer score: {compute_win}\033[39m")
        elif user == "p":
            print(Fore.GREEN + "Computer : paper")
            print("\033[39mIts a tie")
        else:
            print("Invalid input")
        initial_round += 1


    elif pc == "scissor":
        if user == "r":
            print(Fore.GREEN + "Computer : scissor")
            print(Fore.BLUE + "you win this round\033[39m")
            user_win += 1
            print(f"\033[39mYour score: {user_win}")
            print(f"\033[39mcomputer score: {compute_win}\033[39m")
        elif user == "p":
            print(Fore.GREEN + "Computer : scissor")
            print(Fore.RED + "you lost this round")
            compute_win += 1
            print(f"\033[39mYour score: {user_win}")
            print(f"\033[39mcomputer score: {compute_win}\033[39m")
        elif user == "s":
            print(Fore.GREEN + "Computer : scissor")
            print("\033[39mIts a tie")
        else:
            print("Invalid input")
        initial_round += 1


if user_win > compute_win:
    print(Fore.BLUE + Style.BRIGHT + "YOU WIN THE GAME!!\033[39m")
elif compute_win > user_win:
    print(Fore.RED + Style.BRIGHT + "YOU LOSE THE GAME!!\033[39m")
else:
    print("THE GAME ENDED IN A TIE!")