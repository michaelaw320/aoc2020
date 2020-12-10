import math
from typing import List

with open("../input/Day3/input") as f:
    lines = [line for line in f]


def count_trees(slopes: List[str], right: int, down: int):
    trees_count = 0
    pos = 0
    for i in range(0, len(slopes), down):
        line = slopes[i]
        if line[pos % (len(line) - 1)] == "#":
            trees_count += 1
        pos += right
    return trees_count


results = [
    count_trees(lines, 1, 1),
    count_trees(lines, 3, 1),
    count_trees(lines, 5, 1),
    count_trees(lines, 7, 1),
    count_trees(lines, 1, 2),
]

print(f"Trees found: {math.prod(results)}")
