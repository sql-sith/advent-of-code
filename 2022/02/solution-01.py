"""
Solution to the first 2-Dec-2022 puzzle for Advent of Code (https://adventofcode.com)
"""

import re
from enum import Enum

class option(Enum):
    rock = 1
    paper = 2
    scissors = 3

class player(Enum):
    them = 0
    me = 1

class outcome(Enum):
    loss = 0
    tie = 3
    win = 6

outcome_score = {
    outcome.loss: 0,
    outcome.tie: 3,
    outcome.win: 6
}

choice = { 
    "A": {"name": option.rock},
    "B": {"name": option.paper},
    "C": {"name": option.scissors},
    "X": {"name": option.rock},
    "Y": {"name": option.paper},
    "Z": {"name": option.scissors} 
}

choice_score = {
    option.rock: 1,
    option.paper: 2,
    option.scissors: 3
}

game_rule = { 
    option.rock: option.scissors, # rock crushes scissors
    option.paper: option.rock,    # paper covers rock
    option.scissors: option.paper # scissors cuts paper
}

debug = False
total_score = 0
line_count = 0

regex = re.compile(r'\b[a-zA-Z]\b')

with open("./2022/02/input.txt", mode="r") as f:
    for line in f:
        line_count += 1

        their_choice, my_choice = regex.findall(line)
        
        my_option = choice[my_choice]["name"]
        their_option = choice[their_choice]["name"]

        my_choice_score = choice_score[my_option]

        if (my_option, their_option) in game_rule.items():
            match_score = outcome_score[outcome.win]
        elif (their_option, my_option) in game_rule.items():
            match_score = outcome_score[outcome.loss]
        else:
            match_score = outcome_score[outcome.tie]

        total_score += match_score + my_choice_score

        if debug:        
            print(f"line: {line.strip()}; their_choice: {their_choice}; my_choice: {my_choice}")
            print(f"their choice enum {their_option}: my choice enum: {my_option}")
            print(f"choice score: {choice_score}")
            print(f"match score: {match_score}")
            print(f"total score: {total_score}")
            print("")

print(f"\nTotal score is {total_score}. Lines read: {line_count}.")
