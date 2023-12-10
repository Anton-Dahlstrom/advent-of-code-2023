
directions = {"|": {"x": [0, 0], "y": [1, -1]}, "-": {"x": [1, -1], "y": [0, 0]},
               "L": {"x": [1, 0], "y": [1, 0]}, "J": {"x": [0, -1], "y": [1, 0]},
              "7": {"x": [0, -1], "y": [0, -1]}, "F": {"x": [1, 0], "y": [0, -1]}}

with open("day10/day10input.txt", "r") as file:
    lines = file.readlines()
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    grid = [range(0,len(lines[0])), range(0, len(lines))]
    x = 0
    y = 0

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "S":
                x, y = i, j
                # start = [i, j]
    char = lines[y+1][x]
    if char in directions:
        if +1 in directions[char]["y"]:
            print(char)