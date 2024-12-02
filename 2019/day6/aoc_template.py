import pathlib
import sys



def parse(puzzle_input):
    """Parse input"""
    return [line for line in puzzle_input.split('\n')]


def create_orbit_map(data):
    orbit_map = {}
    bodies = set()

    for map_data in data:
        (body,orbit_body) = map_data.split(')')
        orbit_map[orbit_body] = body
        bodies.add(body)
        bodies.add(orbit_body)

    return (orbit_map, bodies)

def calculate_orbit(body,orbits):
    if body not in orbits:
        return []
    return [orbits[body]] + calculate_orbit(orbits[body],orbits)

def orbit_count_checksum(orbits):
    """Calculate checksum of orbit map"""
    return sum(len(calculate_orbit(body,orbits)) for body in orbits)

def calculate_orbital_transfers(start,end,orbits):
    start_path = calculate_orbit(start,orbits)
    end_path = calculate_orbit(end,orbits)
    common_orbit_point = [body for body in start_path if body in end_path][0]
    return start_path.index(common_orbit_point) + end_path.index(common_orbit_point)

def part1(data):
    """Solve part 1"""
    (universal_orbit_map,bodies) = create_orbit_map(data)
    return orbit_count_checksum(universal_orbit_map)


def part2(data):
    """Solve part 2"""
    (universal_orbit_map,bodies) = create_orbit_map(data)
    return calculate_orbital_transfers("YOU","SAN",universal_orbit_map)


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
