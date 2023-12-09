
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
            diff = rows[i][0] - rows[i+1][0]
            rows[i].insert(0, diff)
            print(rows[i])
        print(rows) 
        final += rows[0][0]
        print(final)
print(final)
