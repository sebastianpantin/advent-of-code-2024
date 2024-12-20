from collections import defaultdict

with open("./input.txt") as file:
    data = [line.strip("\n") for line in file.readlines()]

# Part 1
lines = data[:]
width = len(data[0])
lines.extend(["".join([row[i] for row in data]) for i in range(width)])


def find_diagonals(grid):
    rows, cols = len(grid), len(grid[0])

    diagonals = defaultdict(list)
    reverse_diagonals = defaultdict(list)

    for row in range(rows):
        for col in range(cols):
            diagonals[row - col].append(grid[row][col])
            reverse_diagonals[row + col].append(grid[row][col])

    return diagonals, reverse_diagonals


diagonals, reverese_diagonals = find_diagonals(data)
lines.extend(["".join(i) for i in diagonals.values()])
lines.extend(["".join(i) for i in reverese_diagonals.values()])

part1 = sum(line.count("XMAS") + line.count("SAMX") for line in lines)
print("part 1:", part1)

# Part 2

rows, cols = len(data), len(data[0])

count = 0

_letters = {"M", "S"}
for row in range(1, rows - 1):
    for col in range(1, cols - 1):
        if data[row][col] == "A":
            if {data[row - 1][col - 1], data[row + 1][col + 1]} == _letters and {
                data[row - 1][col + 1],
                data[row + 1][col - 1],
            } == _letters:
                count += 1

print("Part 2:", count)
