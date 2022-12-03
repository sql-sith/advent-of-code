"""
Solution to the first 1-Dec-2022 puzzle for Advent of Code (https://adventofcode.com)
"""

debug = False
current_calory_total = 0
current_elf_number = 1
best_elf = {"elf_number": 1, "elf_calories": 0}

with open("./2022/01/input.txt", mode="r") as f:
    for line in f:
        try:
            current_calories = int(line.strip())
            current_calory_total += current_calories
        except ValueError as e:
            if line.strip() == "":
                if current_calory_total > best_elf["elf_calories"]:
                    best_elf["elf_number"] = current_elf_number
                    best_elf["elf_calories"] = current_calory_total

                if debug:
                    print(
                        f"Elf {current_elf_number} is carrying {current_calory_total} calories."
                    )

                current_elf_number += 1
                current_calory_total = 0
            else:
                raise ValueError from e

print(best_elf)
