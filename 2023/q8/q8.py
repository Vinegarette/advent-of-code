import numpy as np

f = "r.txt"
with open(f, "r") as FILE:
    lines = [line.strip() for line in FILE]

    # Construct Adj_List
    instructions = lines[0]
    adj_list = {}
    for line in lines[2:]:
        src, dst = line.split(" = ")

        # Reconstruct dst
        dst = dst[1 : len(dst) - 1].split(", ")
        left, right = dst[0], dst[1]

        adj_list[src] = (left, right)
    # Adj List built
    print(adj_list)

    nodes = [node for node in adj_list.keys() if node[2] == "A"]

    def valid(nodes):
        for node in nodes:
            if node[2] != "Z":
                return False

        return True

    def find_ans(curr, lcms):
        ans = 0

        while curr[2] != "Z":
            for instruction in instructions:
                left, right = adj_list[curr]
                if instruction == "L":
                    curr = left
                else:
                    curr = right

                ans += 1
                if curr[2] == "Z":
                    lcms.append(ans)
                    return

        return

    # Redo with lowest common multiple
    """
    def find_ans():
        ans = 0
        curr = "AAA"
        while curr != "ZZZ":
            for instruction in instructions:
                left, right = adj_list[curr]
                if instruction == "L":
                    curr = left
                else:
                    curr = right

                ans += 1
                if curr == "ZZZ":
                    return ans
    """
    lcms = []
    for node in nodes:
        find_ans(node, lcms)
    print(lcms)
    print(np.lcm.reduce(lcms))
