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

input_translator = { 
    "A": {"translation": option.rock},
    "B": {"translation": option.paper},
    "C": {"translation": option.scissors},
    "X": {"translation": outcome.loss},
    "Y": {"translation": outcome.tie},
    "Z": {"translation": outcome.win} 
}

win_over = { 
    # x: y means "if they play x, i must play y to win."
    option.rock: option.paper, # rock crushes scissors
    option.paper: option.scissors,    # paper covers rock
    option.scissors: option.rock # scissors cuts paper
}

# this will give a dictionary that is the reverse of game_win_rule.
# therefore, x: y means "if they play x, i must play y to lose."
lose_to = dict(zip(win_over.values(), win_over.keys()))

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
        desired_outcome = input_translator[second_letter]["translation"]

        match_score = desired_outcome.value

        if desired_outcome == outcome.win:
            choice_score = win_over[their_option].value
        elif desired_outcome == outcome.loss:
            choice_score = lose_to[their_option].value
        else:
            # in a tie, our choice is the same as theirs:
            choice_score = their_option.value

        total_score += match_score + choice_score

        if debug:        
            print(f"line: {line.strip()}; their option: {their_option}; desired outcome: {desired_outcome}")
            print(f"choice score: {choice_score}")
            print(f"match score: {match_score}")
            print(f"total score for this round: {match_score + choice_score}")
            print(f"overall total so far: {total_score}")
            print("")

print(f"\nTotal score is {total_score}. Lines read: {line_count}.")
