limit = 3
print("\n\n===================")
print("Try to win rock paper scissors in " + str(limit) + " times!")
print("===================")
print("R: rock\nP: paper\nS: scissors")

from random import random
from math import *

tools = ["rock", "paper", "scissors"]
# win pairs of ( player, computer )
win_pairs = [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")]
count_limit = 0
player_won = False
player_rps = ""
computer_rps = ""

def convert_rps(rps):
   if rps == "R" or rps == "r":
      return 0
   elif rps == "P" or rps == "p":
      return 1
   elif rps == "S" or rps == "s":
      return 2
   else:
      return -1

while not player_won and count_limit < limit:
   rdm = floor((random() * 10) % 3)
   computer_rps = tools[rdm]
   player_rps = input("\n\n===============\nRock paper scissors!\n: ")
   valid_rps = convert_rps(player_rps)
   if valid_rps != -1:
      player_rps = tools[valid_rps]
      print("\n>>>> " + player_rps.upper() + "(You) - " + computer_rps.upper() + "(PC)")
   else:
      print("\n***** Please provide a right alphabet")
      count_limit += 1
      continue

   for pair in win_pairs:
      if player_rps == pair[0] and computer_rps == pair[1]:
         player_won = True
         break
   count_limit += 1

print("\n=============")
if player_won:
   print("You win!")
else:
   print("You lose.")
print("=============\n")