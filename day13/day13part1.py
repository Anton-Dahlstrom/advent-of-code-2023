# Find a way to create one solution, then work with pointers to create the rest. Count how many you can create.
# Implement multiple loops over the same string to find all permutations. 
# Needs to start at the correct goal, change index that we turned broken into a working spring and keep going until it fails the first time.
# Then we look at the previous goal until there are no more.

with open("day13/day13input.txt", "r") as file:
    lines = file.readlines()
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()
    failed = False
    for i in range(0, len(lines)):
        print(i)
        print(lines[i])
        if lines[i] == lines[i-1]:
            l = i-1
            r = i
            while l >= 0 and r < len(lines):
                if lines[l] == lines[r]:
                    l -= 1
                    r += 1
                else:
                    failed = True
                    print("no match")
                    print(lines[l], lines[r])
                    print(l, r)
                    break
            if not failed:
                print("match", i)
                break
            else:
                failed = False

    
    previous = ""
    current = ""
    for j in range(0, len(lines[0])):
        for i in range(0, len(lines)):
            current += lines[i][j]
        # print(current)
        if current == previous:
            print("match", j)
            print(current)
            print(previous)
        previous = current
        current = ""
