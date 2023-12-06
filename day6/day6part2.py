import re
with open("day6/day6input.txt", "r") as file:
    
    lines = file.readlines()

    time = int(re.sub("[^0-9]", "", lines[0]))
    distance = int(re.sub("[^0-9]", "", lines[1]))
    
    for i in range(1, time+1):
        if i * (time-i) > distance:
            lowRange = i
            break
    for j in reversed(range(0, time)):
        if j * (time-j) > distance:
            highRange = j
            break
    waysToWin = highRange+1 - lowRange
    print(waysToWin)