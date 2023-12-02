import re

max = {"red": 12, "green": 13, "blue": 14}

total = 0
with open("day2/day2input.txt", "r") as file:
    for line in file:
        hmap = {}
        sum = 1
        line = line.strip()
        game, numbers = line.split(":")
        game = int(game.split(" ")[1])
        numbers = re.split("[,;]",numbers)
        for number in numbers:
            number, color = number.strip().split(" ")
            number = int(number)
            if color in hmap:
                if number > hmap[color]:
                    hmap[color] = number
            else:
                hmap[color] = number
        nums = [hmap[k] for k in hmap]
        for num in nums:
            sum = sum*num
        total += sum
    print(total)
