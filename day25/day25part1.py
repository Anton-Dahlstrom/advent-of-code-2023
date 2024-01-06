with open("day25/day25input.txt", "r") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

    hmap = {}
    for line in lines:
        text = line.split(":")
        node = text[0]
        paths = text[1].strip().split(" ")
        print(paths)
        if node not in hmap:
            hmap[node] = {}
        for path in paths:
            if path not in hmap[node]:
                hmap[node][path] = 1
            if path not in hmap:
                hmap[path] = {node: 1}   
    print(hmap)