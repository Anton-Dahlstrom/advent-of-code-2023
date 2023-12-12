with open("day11/day11input.txt", "r") as file:
    lines = file.readlines()
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()

    # finds the index for empty rows (yindex) and cols (xindex)
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


    # finds coordinates for all the #'s
    coords = []
    for y, line in enumerate(lines):
        for x, value in enumerate(line):
            if value == "#":
                coords.append([y, x]) 

    # Loops through all combinations of coordinates and adds the difference.
    # Looks if there is a y-index of an empty row between the y coordinates of the two #'s
    # Same thing for x coordinates.
    # If the index of an empty row is found we add universe multiplier -1 to the sum of steps
    universeSize = 999999
    sum = 0
    for i in range(0, len(coords)-1):
        for j in range(i+1, len(coords)):
            distance = coords[i][0] - coords[j][0], coords[i][1] - coords[j][1]
            ycoords = [coords[i][0], coords[j][0]]
            xcoords = [coords[i][1], coords[j][1]]
            for index in yindex:
                if index in range(min(ycoords), max(ycoords)):
                    sum += universeSize
            for index in xindex:
                if index in range(min(xcoords), max(xcoords)):
                    sum += universeSize
            for dist in distance:
                if dist < 1:
                    dist *= -1
                sum += dist
    print(sum)