with open("day6/day6input.txt", "r") as file:
    
    lines = file.readlines()
    times = [int(number) for number in lines[0].strip().split(" ") if number.isdigit()]
    distance = [int(number) for number in lines[1].strip().split(" ") if number.isdigit()]
    beatable = [0]*len(times)
    for i, time in enumerate(times):
        for j in range(1, time+1):
            if j * (time-j) > distance[i]:
                beatable[i] += 1
    multiplied = 1
    for num in beatable:
        multiplied *= num
    print(multiplied)