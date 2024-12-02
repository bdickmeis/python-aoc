import pathlib
import sys


MARKER_LENGTH = 4
MESSAGE_LENGTH = 14

def check_chunk(chunk):
    # check if chunk has at least the marker length
    if len(chunk) < MARKER_LENGTH:
        #print('Marker length not reached')
        return False
    
    last_chunk = chunk[-MARKER_LENGTH:] if len(chunk)>MARKER_LENGTH else chunk
    # quick scan last 4 character in chunk for repeats
    freq = {}
    for char in last_chunk:
        #print(f'Char : {char} - found {last_chunk.count(char)}')
        freq[char] = last_chunk.count(char)
    
    print(f'{freq}')
    
    # check for duplicates -> any frequence count higher than 1 ?
    if any([char for char in freq.keys() if freq[char] > 1]):
        #print(f'Found duplicates in {chunk:}')
        return False
    
    print(f'Candidate marker found : {last_chunk}')
    return True
    
def check_message(chunk):
    # check if chunk has at least the marker length
    if len(chunk) < MESSAGE_LENGTH:
        #print('Marker length not reached')
        return False
    
    last_chunk = chunk[-MESSAGE_LENGTH:] if len(chunk)>MESSAGE_LENGTH else chunk
    # quick scan last 4 character in chunk for repeats
    freq = {}
    for char in last_chunk:
        freq[char] = last_chunk.count(char)
    
    # check for duplicates -> any frequence count higher than 1 ?
    if any([char for char in freq.keys() if freq[char] > 1]):
        return False
    
    print(f'Candidate marker found : {last_chunk}')
    return True    
        

def parse(puzzle_input):
    """Parse input"""
    return puzzle_input


def part1(data):
    """Solve part 1"""
    chunk = ""
    for i,c in enumerate(data):
        chunk += c
        if check_chunk(chunk):
            print(f'Marker found: {chunk[-MARKER_LENGTH:]} at {i+1}')
            return i+1

def part2(data):
    chunk = ""
    for i,c in enumerate(data):
        chunk += c
        if check_message(chunk):
            print(f'Marker found: {chunk[-MESSAGE_LENGTH:]} at {i+1}')
            return i+1


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f'Solving with input : {path}')
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
