from collections import defaultdict

with open("./input.txt") as file:
    data = [line.strip("\n") for line in file.readlines()]

separator = data.index("")
rules: dict[int, set] = defaultdict(set)
for rule in data[:separator]:
    a, b = map(int, rule.split("|"))
    rules[a].add(b)
updates = [list(map(int, i.split(","))) for i in data[separator + 1 :]]


def is_valid(rules, update):
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if update[j] not in rules[update[i]]:
                return False
    return True


def fix(rules, update):
    filtered_rules = defaultdict(set)
    for i in update:
        filtered_rules[i] = rules[i] & set(update)

    ordered_keys = sorted(
        filtered_rules, key=lambda k: len(filtered_rules[k]), reverse=True
    )

    return ordered_keys


# part 1


sum = 0
for update in updates:
    if is_valid(rules, update):
        sum += update[len(update) // 2]

print("Part 1:", sum)

# part 2
sum = 0
for update in updates:
    if not is_valid(rules, update):
        fixed = fix(rules, update)
        sum += fixed[len(update) // 2]


print("Part 2:", sum)
