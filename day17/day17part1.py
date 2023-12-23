
with open("day17/day17input.txt", "r") as file:
    lines = file.readlines()
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()
    ymax = len(lines)
    xmax = len(lines[0])
    # while 0 <= x < xmax and 0 <= y < ymax: 
    #     if y == ymax-1 and x == xmax-1:
    #         print("FINISHED")
    #         break
    for k in range(0, len(lines)):
        lines[k] = [int(char) for char in lines[k]]
        
    for i in range(1, len(lines)):
        lines[i][0] += lines[i-1][0]
    for j in range(1, len(lines[0])):
        lines[0][j] += lines[0][j-1]

    for a in range(1, len(lines)):
        for b in range(1, len(lines[0])):
            lines[a][b] += min(lines[a-1][b], lines[a][b-1])

    for line in lines:
        print(line)
# 241
# 321
# 325
        
# 267
# 578
# 89,13