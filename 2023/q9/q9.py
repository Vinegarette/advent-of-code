f = "r.txt"


def solve(line):
    line = list(map(int, line.split(" ")))
    print(line)
    lines = []

    while len(line) > 1:
        curr = []
        lines.append(line)
        for i in range(1, len(line)):
            diff = line[i] - line[i - 1]
            curr.append(diff)

        # Check if all 0
        is_zero = True
        for c in curr:
            if c != 0:
                is_zero = False
                break

        if is_zero:
            lines.append(curr)
            break
        else:
            line = curr
    # Use curr
    ans = 0
    lines = lines[::-1]
    """new_lines = []
    for line in lines:
        new_lines.append(line[::-1])
    # print(lines)
    lines = new_lines"""
    lines = list(map(lambda x: x[::-1], lines))

    for i in range(1, len(lines)):
        lower, upper = lines[i - 1][-1], lines[i][-1]
        print(lower, upper)
        lines[i].append(upper - lower)
    print(lines)
    return lines[-1][-1]


with open(f, "r") as FILE:
    ans = 0

    lines = [line.strip() for line in FILE]
    for line in lines:
        ans += solve(line)
    print(ans)
