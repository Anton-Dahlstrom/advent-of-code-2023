import re

max = {"red": 12, "green": 13, "blue": 14}
total = 0
with open("day2/day2input.txt", "r") as file:
    for line in file:
        found = False
        line = line.strip()
        game, numbers = line.split(":")
        game = int(game.split(" ")[1])
        numbers = re.split("[,;]",numbers)
        for number in numbers:
            number, color = number.strip().split(" ")
            if int(number) > max[color]:
                found = True
                break
        if not found:
            total += game
    print(total)
