
with open("day9/day9input.txt", "r") as file:
    lines = file.readlines()
    hmap = {}
    rows = []
    final = 0
    for line in lines:
        rows = []
        rows.append([int(num) for num in line.strip().split(" ")])
        finished = False
        while finished == False:
            temp = []
            finished = True
            for i in range (1, len(rows[-1])):            
                diff = rows[-1][i] - rows[-1][i-1]
                temp.append(diff)
                if diff != 0:
                    finished = False
            rows.append(temp)          
        for i in reversed(range(0, len(rows)-1)):
            nextNum = rows[i][-1] + rows[i+1][-1]
            rows[i].append(nextNum)
        final += rows[0][-1]
print(final)
