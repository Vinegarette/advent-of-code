import math

filename = "part1.txt"
with open(filename, "r") as FILE:
    ans = 0
    for line in FILE.readlines():
        dic = {"red": 0, "blue": 0, "green": 0}

        start = line.split(":")
        # Get id
        id = start[0].split(" ")[1]

        # Take minimums now
        info = "".join(start[1:]).split(";")
        for section in info:
            items = section.split(",")
            for item in items:
                item = item.strip()
                count, colour = item.split(" ")
                dic[colour] = max(dic[colour], int(count))

        val = dic["red"] * dic["blue"] * dic["green"]

        ans += val

    print(ans)
