import math
import threading

filename = "q5.txt"


def process_seed_range(start, length, layers, result):
    local_min = math.inf
    for seed in range(start, start + length):
        local_min = min(local_min, find_lowest_location(seed, layers))
        print(local_min)
    with result_lock:
        result[0] = min(result[0], local_min)


with open(filename, "r") as FILE:
    ans = 0

    # Process lines
    lines = []
    curr = []
    for line in FILE:
        if line == "\n":
            lines.append(curr)
            curr = []
        else:
            curr.append(line.strip())

    lines.append(curr)
    # Set up each instance
    # Each line is a list of strings

    # Part B Set Up Seeds
    seeds = lines[0][0].split(": ")[1].split(" ")

    layers = [lines[i][1:] for i in range(1, len(lines))]

    def layer_map_int(layer):
        ans = []
        for string in layer:
            ans.append([int(number) for number in string.split(" ")])

        return ans

    layers = list(map(layer_map_int, layers))

    ans = math.inf

    def find_lowest_location(seed, layers):
        # For each seed, walk thru each layer...
        location = math.inf

        curr = seed
        for layer in layers:
            # Check if curr is valid in this layer
            # If not in any range, the curr remains the same
            # print(f"Curr layer is {layer}")
            for range_map in layer:
                destination_range, source_range, length_range = range_map
                # print(destination_range, source_range, length_range)
                if curr >= source_range and curr < source_range + length_range:
                    """print(
                        f"Found in between {source_range} and {source_range + length_range}, destination_range {destination_range} and curr {curr}"
                    )
                    print(f"New curr to be {curr - source_range + destination_range}")
                    """
                    curr = (curr - source_range) + destination_range
                    break
            # print(curr)
        # print(f"Final location is {curr} for seed {seed}")
        return curr

    seeds = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]
    print(seeds)
    result = [math.inf]  # Shared result
    result_lock = threading.Lock()  # Lock for updating the result
    threads = []

    for start, length in seeds:
        start = int(start)
        length = int(length)
        thread = threading.Thread(
            target=process_seed_range, args=(start, length, layers, result)
        )
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    ans = result[0]
    print(ans)
