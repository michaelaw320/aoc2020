with open("../input/Day3/input") as f:
    lines = [line for line in f]

trees_count = 0

pos = 0

for line in lines:
    if line[pos % (len(line) - 1)] == "#":
        trees_count += 1
    pos += 3

print(f"Trees found: {trees_count}")
