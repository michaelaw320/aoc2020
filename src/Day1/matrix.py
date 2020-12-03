from typing import List, Tuple

with open("../input/Day1/input") as f:
    l = [int(line) for line in f]

x = l
y = l

matrix = [[i + j for j in y] for i in x]


def find_2020(matrix: List[List[int]]) -> Tuple[int, int]:
    for i in range(len(x)):
        for j in range(len(y)):
            if matrix[i][j] == 2020:
                return (i, j)


i, j = find_2020(matrix)
print(f"Result: {x[i]*y[j]}")
