from functools import reduce


def part_a():
    filename = "q6.txt"

    with open(filename, "r") as FILE:
        # Process
        lines = [line.strip() for line in FILE]
        print(lines)
        times = [int(num) for num in lines[0].split(":")[1].split(" ") if num != ""]
        distances = [int(num) for num in lines[1].split(":")[1].split(" ") if num != ""]

        print(times)
        print(distances)
        ans = []

        for time, distance in zip(times, distances):
            # No point in considering not holding, and holding all
            wins = 0
            for speed in range(0, time + 1):
                # Check if speed is good enough
                time_left = time - speed
                traveled = speed * time_left
                if traveled > distance:
                    wins += 1
            ans.append(wins)

        print(reduce((lambda x, y: x * y), ans))


def part_b():
    filename = "q6.txt"

    with open(filename, "r") as FILE:
        # Process
        lines = [line.strip() for line in FILE]

        times = [int(num) for num in lines[0].split(":")[1].split(" ") if num != ""]
        distances = [int(num) for num in lines[1].split(":")[1].split(" ") if num != ""]

        time = int("".join([str(num) for num in times]))
        distance = int("".join([str(num) for num in distances]))
        ans = 0

        for speed in range(0, time + 1):
            # Check if speed is good enough
            time_left = time - speed
            traveled = speed * time_left
            if traveled > distance:
                ans += 1

        print(ans)


if __name__ == "__main__":
    # part_a()
    part_b()
