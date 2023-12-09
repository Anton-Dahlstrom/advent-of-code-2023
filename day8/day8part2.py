import re
with open("day8/day8input.txt", "r") as file:
    values = {"T": 10, "J": 11, "Q": 12, "K": 13}

    lines = file.readlines()
    hmap = {}
    current = "AAA"
    start = []
    for line in lines:
        row = re.sub("[^a-zA-Z ]", "", line).strip().split()
        if len(row) == 3:
            hmap[row[0]] = {"L": row[1], "R": row[2]}
            if row[0][2] == "A":
                start.append(row[0])

    loopList = []
    for i in range(0, len(start)):
        loop = True
        starter = start[i]
        attempts = 0
        while loop:
            for char in lines[0].strip():
                if not loop:
                    break
                starter = hmap[starter][char]
                attempts += 1
                if starter[2] == "Z":
                    loop = False
                    loopList.append(attempts)
                elif starter[2] == "A":
                    loop = False

    def prime_factors(n):
        factors = []
        d = 2
        while n > 1:
            while n % d == 0:
                factors.append(d)
                n /= d
            d = d + 1
        return factors
     
    toMulti = {}
    for num in loopList:
        primes = prime_factors(num)
        for prime in primes:
            if prime not in toMulti:
                toMulti[prime] = 1
    total = 1
    for number in toMulti:
        total = total * number
    print(total)
