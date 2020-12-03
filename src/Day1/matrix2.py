from typing import List, Tuple

with open("../input/Day1/input") as f:
    l = [int(line) for line in f]

x = l
y = l
z = l

matrix = [[[i + j + k for k in z] for j in y] for i in x]


def find_2020(matrix: List[List[List[int]]]) -> Tuple[int, int, int]:
    for i in range(len(x)):
        for j in range(len(y)):
            for k in range(len(z)):
                if matrix[i][j][k] == 2020:
                    print(f"Found 2020 in: {i} {j} {k}")
                    print(f"Three nums: {x[i], y[j], z[k]}")
                    return (i, j, k)


i, j, k = find_2020(matrix)
print(f"Result: {x[i]*y[j]*z[k]}")
