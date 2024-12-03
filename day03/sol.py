import re

with open("./input.txt") as file:
    data = file.read().strip()

# part 1

pattern = r"mul\((\d+),(\d+)\)"
muls = [(int(a), int(b)) for a, b in re.findall(pattern, data)]
part1 = sum(mul[0] * mul[1] for mul in muls)
# part 2

pattern = r"(mul\((\d+),(\d+)\)|do\(\)|don't\(\))"
matches = re.findall(pattern, data)
part2 = 0
do = True
for i, j, k in matches:
    if i == "don't()":
        do = False
    elif i == "do()":
        do = True
    else:
        if do:
            part2 += int(j) * int(k) 




print(f"Part 1: {part1}, Part 2: {part2}")

