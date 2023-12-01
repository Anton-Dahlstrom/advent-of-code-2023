translations = {"one": "1", "two": "2", "three": "3", "four": "4", 
                "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

with open("day1/day1input.txt", "r") as file:
    total = 0
    for line in file:
        toAdd = ""
        word = ""
        line = line.strip()
        found = False

        for i in range(0, len(line)): 
            if found:
                found = False
                break    
            if line[i].isnumeric():
                word = ""
                toAdd += line[i]
                break
            word += line[i]
            for key in translations:
                if key in word:
                    toAdd += translations[key]
                    found = True
                    word = ""
                    break

        for i in reversed(range(0, len(line))): 
            if found:
                found = False
                break  
            if line[i].isnumeric():   
                word = "" 
                toAdd += line[i]
                break
            word = line[i] + word
            for key in translations:
                if key in word:
                    toAdd += translations[key]
                    found = True
                    break

        toAdd = int(toAdd)
        total += toAdd
    print(total)
