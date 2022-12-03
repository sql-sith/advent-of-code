"""
Solution to the second 1-Dec-2022 puzzle for Advent of Code (https://adventofcode.com)
"""

from sortedcontainers import SortedList

debug = False
number_of_elves = 3
current_elf_number = 1
current_calory_total = 0
best_elves = SortedList()
best_elves.add(0)

with open("./2022/01/input.txt", mode="r") as f:
    for line in f:
        try:
            current_calories = int(line.strip())
            current_calory_total += current_calories
        except ValueError as e:
            if line.strip() == "":

                if len(best_elves) < number_of_elves:
                    best_elves.add(current_calory_total)
                elif current_calory_total > best_elves[0]:
                    best_elves.pop(0)
                    best_elves.add(current_calory_total)
                    print(f"Adding elf {current_elf_number} with {current_calory_total} calories.")

                if debug:
                    print(
                        f"Elf {current_elf_number} is carrying {current_calory_total} calories."
                    )

                current_elf_number += 1
                current_calory_total = 0
            else:
                raise ValueError from e

print(f"The three largest calorie loads are {best_elves} and add up to {sum(best_elves)} total calories.")
