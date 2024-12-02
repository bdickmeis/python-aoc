import pathlib
import sys



def parse(puzzle_input):
    """Parse input"""
    return [[i for i in wire.split(',')] for wire in puzzle_input.split('\n')]

def dist(p1, p2=(0, 0)) -> int:
    """Calculates the Manhattan distance between two points"""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def trace(step: str, pos: tuple) -> list:
    """Draws the line formed by applying a step (`step`) to a given coordinate (`pos`).

        Args:
            `step`: The step to be taken.
            `pos`: The position to which the step should be applied.
        Returns:
            (list): A list of coordinates that define the line.
    """
    shift = int(step[1:])
    direction = step[0]
    x = pos[0]
    y = pos[1]
    if direction == "D":
        line = [(x, y-j) for j in range(1, shift+1)]
    elif direction == "U":
        line = [(x, y+j) for j in range(1, shift+1)]
    elif direction == "L":
        line = [(x-i, y) for i in range(1, shift+1)]
    elif direction == "R":
        line = [(x+i, y) for i in range(1, shift+1)]
    return line

def draw(pos: tuple, path: list) -> list:
    """Draws the graph formed by following a sequence of steps (`path`) from a given starting position (`pos`)."""
    graph = []
    for step in path:
        line = trace(step, pos)
        pos = line[-1]  # Update `pos`.
        graph += line
    return graph

def intersect(paths: list) -> tuple:
    """Draws the graphs formed by following the two provided paths and finds their intersection.

        Args:
            `paths`: A list of two elements, corresponding to the paths for the two wires.
        Returns:
            (tuple): A 3-tuple representing the graphs of the three wires and their intersections.
                `graph_1 (list)`: Graph of the first wire.
                `graph_2 (list)`: Graph of the second wire.
                `crosses`: Set of points where the two wires cross each other.
    """
    graph_1, graph_2 = draw((0, 0), paths[0]), draw((0, 0), paths[1])
    crosses = set(graph_1) & set(graph_2)
    return crosses, graph_1, graph_2

def reaches(paths: list) -> dict:
    """Finds the distance travelled by each wire to their various points of intersection.

        Args:
            `paths`: A list of two elements, corresponding to the paths for the two wires.
        Returns:
            (dict): A dictionary mapping each point of intersection to the distances the two wires take to reach it.
    """
    crosses, graph_1, graph_2 = intersect(paths)
    dct = {point: [None, None] for point in crosses}
    for idx, pair in enumerate(graph_1):
        if pair in crosses:
            dct[pair][0] = dct[pair][0] or idx+1
    for idx, pair in enumerate(graph_2):
        if pair in crosses:
            dct[pair][1] = dct[pair][1] or idx+1
    return dct


def part1(data):
    """Solve part 1"""
    return min(dist(cross) for cross in intersect(data)[0])


def part2(data):
    """Solve part 2"""
    return min(sum(pair) for pair in reaches(data).values())


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
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
