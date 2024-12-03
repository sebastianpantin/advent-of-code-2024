import re

with open("./input.txt") as file:
    data = file.read().strip().split("\n")

reports = [list(map(int, re.findall("\\d+", x))) for x in data]


# Part 1
def safe1(report):
    return all(
        (1 <= abs(n1 - n2) <= 3)
        and (report == sorted(report) or report == sorted(report)[::-1])
        for n1, n2 in zip(report, report[1:])
    )


safe1_ans = sum(safe1(report) for report in reports)


# Part 2

def safe2(report):
    return any(safe1(report[:i] + report[i + 1:]) for i in range(len(report)))

safe2_ans = sum(safe2(report) for report in reports)


print(f"Part 1: {safe1_ans}, Part 2: {safe2_ans}")
