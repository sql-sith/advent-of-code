"""
Solution to the first 2-Dec-2022 puzzle for Advent of Code (https://adventofcode.com)
"""

import re
from enum import Enum

class opt(Enum):
    rock = 1
    paper = 2
    scissors = 3

class player(Enum):
    them = 0
    me = 1

class win_loss_score(Enum):
    loss = 0
    tie = 3
    win = 6

choice = { 
    "A": {"name": opt.rock, "type": player.them},
    "B": {"name": opt.paper, "type": player.them},
    "C": {"name": opt.scissors, "type": player.them},
    "X": {"name": opt.rock, "type": player.me, "score": 1},
    "Y": {"name": opt.paper, "type": player.me, "score": 2},
    "Z": {"name": opt.scissors, "type": player.me, "score": 3} 
}

game_rule = { 
    opt.rock: opt.scissors, # rock crushes scissors
    opt.paper: opt.rock,    # paper covers rock
    opt.scissors: opt.paper # scissors cuts paper
}

debug = True
total_score = 0
line_count = 0

regex = re.compile(r'\b[a-zA-Z]\b')

with open("./2022/02/input.txt", mode="r") as f:
    for line in f:
        line_count += 1

        their_choice, my_choice = regex.findall(line)
        
        my_opt = choice[my_choice]["name"]
        their_opt = choice[their_choice]["name"]

        choice_score = choice[my_choice]["score"]

        if (my_opt, their_opt) in game_rule.items():
            match_score = win_loss_score.win.value
        elif (their_opt, my_opt) in game_rule.items():
            match_score = win_loss_score.loss.value
        else:
            match_score = win_loss_score.tie.value

        total_score += match_score + choice_score

        if debug:        
            print(f"line: {line.strip()}; their_choice: {their_choice}; my_choice: {my_choice}")
            print(f"their choice enum {their_opt}: my choice enum: {my_opt}")
            print(f"choice score: {choice_score}")
            print(f"match score: {match_score}")
            print(f"total score: {total_score}")
            print("")

print(f"\nTotal score is {total_score}. Lines read: {line_count}.")
