from collections import Counter

with open("./input.txt") as file:
    data = file.read().strip().split("\n")

ll, lr = zip(*[map(int, x.split()) for x in data])

# Part 1

total = sum((abs(l1 - l2) for l1, l2 in zip(sorted(ll), sorted(lr))))

# Part 2


counter = Counter(lr)
sim_score = sum((x * counter[x] for x in ll))


print(f"Part 1: {total}, Part 2: {sim_score}")
