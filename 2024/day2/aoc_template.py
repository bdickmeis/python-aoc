# aoc_template.py

import pathlib
import sys


def parse(puzzle_input):
    """Parse input."""
    reports = []
    for line in puzzle_input.split("\n"):
        reports.append([int(level) for level in line.split(" ")])
    return reports


def calculate_delta(report):
    return [-(i - j) for i, j in zip(report[:-1], report[1:])]


def check_safety(report):

    delta = calculate_delta(report)

    if all(val > 0 for val in delta) and all(abs(val) <= 3 for val in delta):
        # print(f"{report} Safe : {delta}")
        return True

    if all(val < 0 for val in delta) and all(abs(val) <= 3 for val in delta):
        # print(f"{report} Safe : {delta}")
        return True

    return False


def check_dampener(report):
    tolerance_count = 0
    max_tolerance = 1

    for i in range(len(report)):
        dampened_report = []
        for idx, ele in enumerate(report):
            if idx != i:
                dampened_report.append(ele)
                
        if check_safety(dampened_report):
            tolerance_count += 1

    # check if we have at least one tolarance detected (no tolerance => Unsafe)
    # if we have a tolarance - check if it's only 1 difference
    if tolerance_count > 0 and tolerance_count < len(report) - max_tolerance:
        return True

    return False


def part1(data):
    """Solve part 1."""
    safe_count = 0
    for report in data:
        safe_count += 1 if check_safety(report) else 0

    return safe_count


def part2(data):
    """Solve part 2."""
    safe_count = 0
    for report in data:
        if check_safety(report):
            safe_count += 1
        elif check_dampener(report):
            safe_count += 1
    return safe_count


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
