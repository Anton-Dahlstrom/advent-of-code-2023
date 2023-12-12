with open("day11/day11input.txt", "r") as file:
    lines = file.readlines()
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    yindex = []
    xindex = []
    for i, line in enumerate(lines):
        if not "#" in line:
            yindex.append(i)

    for col in range(0, len(lines[0])):
        found = False
        for row in range(0, len(lines)):
            if lines[row][col] == "#":
                found = True
                break
        if not found:
            xindex.append(col)

    empty = "."*len(lines[0])
    count = 0
    for index in yindex:
        lines.insert(index + count, empty)
        count += 1
    count = 0
    for index in xindex:
        for i, line in enumerate(lines):
            line = list(line)
            line.insert(index + count, ".")
            line = "".join(line)
            lines[i] = line
        count += 1

    coords = []
    for y, line in enumerate(lines):
        for x, value in enumerate(line):
            if value == "#":
                coords.append([y, x]) 
    sum = 0
    for i in range(0, len(coords)-1):
        for j in range(i+1, len(coords)):
            distance = coords[i][0] - coords[j][0], coords[i][1] - coords[j][1]
            for dist in distance:
                if dist < 1:
                    dist *= -1
                sum += dist
    print(sum)