filename = "example.txt"


def iterate(grid, r, c, direction, visited):
    x = c
    num = []
    while (x > -1 and x < len(grid[0])) and grid[r][x].isnumeric():
        if (r, x) in visited:
            return 0
        visited.add((r, x))
        num.append(grid[r][x])
        x += direction

    return num


def find_number(grid, r, c, visited):
    # Iterate left and then iterate right

    left_half = iterate(grid, r, c, -1, visited)
    left_half = left_half[::-1]
    right_half = iterate(grid, r, c + 1, 1, visited)

    return int("".join(left_half + right_half))


if __name__ == "__main__":
    with open(filename, "r") as FILE:
        # Create a 2D Matrix?
        grid = []

        for line in FILE.readlines():
            curr = [c for c in line.strip()]
            grid.append(curr)

        print(grid)

        ans = 0
        # Iterate thru grid, and if not a num and a '.'
        # Then must inspect the index for neighbouring numbers!

        m, n = len(grid), len(grid[0])

        symbol_indexes = []

        for r in range(m):
            for c in range(n):
                if not grid[r][c].isnumeric() and grid[r][c] != ".":
                    symbol_indexes.append((r, c))

        # Find all neighbouring numbers...
        for r, c in symbol_indexes:
            # Only add together those with exactly 2 numbers
            local_seen = set()
            count = 0
            nums = []
            for x, y in [
                [0, 1],
                [1, 0],
                [-1, 0],
                [0, -1],
                [1, 1],
                [-1, -1],
                [1, -1],
                [-1, 1],
            ]:
                nr, nc = r + x, c + y
                # Test if number
                if (
                    nr > -1
                    and nr < m
                    and nc > -1
                    and nc < n
                    and grid[nr][nc].isnumeric()
                    and (nr, nc) not in local_seen
                ):
                    count += 1
                    nums.append(find_number(grid, nr, nc, local_seen))

            if count == 2:
                ans += nums[0] * nums[1]

        print(ans)
