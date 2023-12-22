
with open("day16/day16input.txt", "r") as file:
    lines = file.readlines()
    hmap = {}
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()
    ymax = len(lines)
    xmax = len(lines[0])
    dirs = {"r": 1, "l": -1, "u": -1, "d": 1}
    beams = [[0, 0, "r"]]
    searched = {(0,0): ["r"]}

    while beams:
        running = 0
        y, x, direction = beams.pop()
        while 0 <= x < xmax and 0 <= y < ymax:
            current = lines[y][x] 
            if current != ".":
                if current == "|":
                    if direction == "l" or direction == "r":
                        if (y,x) not in searched:
                            searched[y,x] = 1
                            beams.append([y, x, "u"])
                        direction = "d" 
                elif current == "-":
                    if direction == "u" or direction == "d":
                        if (y,x) not in searched:
                            searched[y,x] = 1
                            beams.append([y, x, "r"])
                        direction = "l"
                elif current == "/":
                    print(y, x, direction)
                    if direction == "u":
                        direction = "r"
                    elif direction == "d":
                        direction = "l"
                    elif direction == "l":
                        direction = "d"
                    elif direction == "r":
                        direction = "u"
                    print(direction)
                elif current == "\\":
                    if direction == "u":
                        direction = "l"
                    elif direction == "d":
                        direction = "r"
                    elif direction == "l":
                        direction = "u"
                    elif direction == "r":
                        direction = "d"
            if (y,x) not in hmap:
                hmap[y, x] = 1
            if direction == "r" or direction == "l":
                x += dirs[direction]
            else:
                y += dirs[direction]
            running += 1
            if running > 10000:
                break
print(len(hmap))