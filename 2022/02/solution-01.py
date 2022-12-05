"""
Solution to the first 2-Dec-2022 puzzle for Advent of Code (https://adventofcode.com)
"""

import re
from enum import Enum

class option(Enum):
    rock = 1
    paper = 2
    scissors = 3

class outcome(Enum):
    loss = 0
    tie = 3
    win = 6

outcome_score = {
    outcome.loss: 0,
    outcome.tie: 3,
    outcome.win: 6
}

input_translator = { 
    "A": {"translation": option.rock},
    "B": {"translation": option.paper},
    "C": {"translation": option.scissors},
    "X": {"translation": option.rock},
    "Y": {"translation": option.paper},
    "Z": {"translation": option.scissors} 
}

choice_score = {
    option.rock: 1,
    option.paper: 2,
    option.scissors: 3
}

win_over = { 
    option.rock: option.scissors, # rock crushes scissors
    option.paper: option.rock,    # paper covers rock
    option.scissors: option.paper # scissors cuts paper
}

debug = False
total_score = 0
line_count = 0

regex = re.compile(r'\b[a-zA-Z]\b')

print("")
with open("./02/input.txt", mode="r") as f:
    for line in f:
        line_count += 1

        first_letter, second_letter = regex.findall(line)
        
        their_option = input_translator[first_letter]["translation"]
        my_option = input_translator[second_letter]["translation"]

        my_choice_score = choice_score[my_option]

        if (my_option, their_option) in win_over.items():
            match_score = outcome.win.value
        elif (their_option, my_option) in win_over.items():
            match_score = outcome.loss.value
        else:
            match_score = outcome.tie.value

        total_score += match_score + my_choice_score

        if debug:        
            print(f"line: {line.strip()}; their option: {their_option}; my option: {my_option}")
            print(f"choice score: {my_choice_score}")
            print(f"match score: {match_score}")
            print(f"total score for this round: {match_score + my_choice_score}")
            print(f"overall total so far: {total_score}")
            print("")

print(f"\nTotal score is {total_score}. Lines read: {line_count}.")
