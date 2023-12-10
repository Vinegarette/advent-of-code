from collections import deque


f = "r.txt"
lines = list(map(lambda x: x.strip(), open(f, "r").readlines()))


# Construct pathes for each type
dir_list = {
    "|": [[1, 0], [-1, 0]],
    "-": [[0, 1], [0, -1]],
    "L": [[-1, 0], [0, 1]],
    "J": [[-1, 0], [0, -1]],
    "7": [[1, 0], [0, -1]],
    "F": [[1, 0], [0, 1]],
}


# BFS from start, find distance
m, n = len(lines), len(lines[0])

grid = list(map(lambda x: list(x), lines))
print(grid)

# Lessgo
queue = deque()
seen = set()
for r in range(m):
    for c in range(n):
        if grid[r][c] == "S":
            # BFS!
            queue.append((r, c))
            seen.add((r, c))

is_vertical = False


def check_s(r, c):
    is_vertical = False
    print("Checking S")
    dir_list = [
        (r + 1, c, set("|LJ")),
        (r - 1, c, set("|7F")),
        (r, c + 1, set("-J7")),
        (r, c - 1, set("-LF")),
    ]

    seen.add((r, c))
    for nr, nc, valid in dir_list:
        if (
            nr > -1
            and nr < m
            and nc > -1
            and nc < n
            and (nr, nc) not in seen
            and grid[nr][nc] in valid
        ):
            queue.append((nr, nc))
            seen.add((nr, nc))
            if nr == r - 1 and c == nc:
                is_vertical = True
    print(queue)
    return is_vertical


print(seen)
ans = 0
while queue:
    length = len(queue)
    for _ in range(length):
        r, c = queue.popleft()
        # Check dirs
        if grid[r][c] == "S":
            is_vertical = check_s(r, c)
        else:
            # Check adj_dirs
            dirs = dir_list[grid[r][c]]
            for x, y in dirs:
                nr, nc = r + x, c + y
                if nr > -1 and nr < m and nc > -1 and nc < n and (nr, nc) not in seen:
                    # Add to queue!
                    queue.append((nr, nc))
                    seen.add((nr, nc))
    # print(queue)
    ans += 1

inside = 0
# Part 2
vertical = set("LJ|")
for r in range(m):
    in_grid = False
    for c in range(n):
        if (r, c) in seen:
            if grid[r][c] in vertical or (grid[r][c] == "S" and is_vertical):
                in_grid = not in_grid
        else:
            inside += in_grid

print(f"Furthest distance reached is {ans - 1}")
print(f"Inside are {inside}")
