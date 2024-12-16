with open("./input.txt") as file:
    data = [line.strip("\n") for line in file.readlines()]

directions = ((-1, 0), (0, 1), (1, 0), (0, -1))


map = [list(line) for line in data]


def get_init_pos():
    rows, cols = len(map), len(map[0])
    for i in range(rows):
        for j in range(cols):
            if map[i][j] == "^":
                return (i, j)


# Part 1
pos = get_init_pos()
idx = 0

rows, cols = len(map), len(map[0])
visited = set()
visited.add((pos[0], pos[1]))

while True:
    dir = directions[idx]
    n = (pos[0] + dir[0], pos[1] + dir[1])

    # Leaving the map
    if n[0] < 0 or n[0] >= rows or n[1] < 0 or n[1] >= cols:
        break

    if map[n[0]][n[1]] == "#":
        idx = (idx + 1) % 4  # Turn 90 degrees
        continue
    else:
        visited.add((n[0], n[1]))
        pos = n


print("Part 1:", len(visited))
