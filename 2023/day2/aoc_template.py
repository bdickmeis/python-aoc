import pathlib
import sys

max_r = 12
max_g = 13
max_b = 14

def parse_rgb(move : str):
    r = 0
    g = 0
    b = 0
    for cube in move.split(', '):
        (number,color) = cube.split(' ')
        match color:
            case 'red':
                r = int(number)
            case 'green':
                g = int(number)
            case 'blue':
                b = int(number)
        
    return (r,g,b)

def parse(puzzle_input):
    """Parse input"""
    cube_game = {}
    
    for gameline in puzzle_input.split('\n'):
        
        id = int(gameline.split(': ')[0].split(' ')[1])
        move_list = []
        moves = gameline.split(': ')[1]
        for move in moves.split('; '):
            (r,g,b) = parse_rgb(move)
            move_list.append((r,g,b))
        
        cube_game[id] = move_list
    
    return cube_game
        

def is_game_possible(movelist : list):
    for (r,g,b) in movelist:
        if r > max_r or g > max_g or b > max_b:
            return False    
    return True

def get_power_set(movelist : list):
    
    (min_r,min_g,min_b) = movelist[0]

    for (r,g,b) in movelist[1:]:
        min_r = r if r > min_r else min_r
        min_g = g if g > min_g else min_g
        min_b = b if b > min_b else min_b

    min_r = 1 if min_r == 0 else min_r
    min_g = 1 if min_g == 0 else min_g
    min_b = 1 if min_b == 0 else min_b

    return min_r*min_g*min_b


def part1(data):
    """Solve part 1"""
    possible_games = []
    for id,movelist in data.items():
        if is_game_possible(movelist):
            possible_games.append(id)
    
    return sum(possible_games)


def part2(data):
    """Solve part 2"""
    powers = []
    for movelist in data.values():
        powers.append(get_power_set(movelist))
    
    return sum(powers)



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
