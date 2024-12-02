import pathlib
import sys

INSTRUCTION_MARKER = "$"
CD_MARKER = "cd"
LS_MARKER = "ls"
CD_UP_MARKER = ".."
ROOT_MARKER = "/"
DIR_MARKER = "dir"


class File:
    def __init__(self, name, size, parent) -> None:
        self.name = name
        self.size = size
        self.parent = parent
        self.children = None
        self.size_below = 0

    def get_size(self,threshold=None):
        return self.size

    def __repr__(self):
        return f"{self.name} (file,size={self.size})"


class Folder:
    def __init__(self, name, parent=None) -> None:
        self.name = name
        self.children = {}
        self.size = 0
        self.parent = parent
        self.size_below = 0
        self.marked_for_deletion = False

    def add_child(self, child):
        self.children[child.name] = child
        self.get_size()

    def get_size(self,threshold=None):
        total = sum([child.get_size() for child in self.children])
        if threshold:            
            self.marked_for_deletion = total < threshold

        return total
    
    def check_del(self):
        return [child for child in self.children if isinstance(child,Folder) and child.marked_for_deletion]

    def __repr__(self):
        out_string = f"{self.name} (dir, size={self.get_size()})\n"
        for child in self.children:
            out_string += f" - {child}\n"
        return out_string


def parse(puzzle_input):
    """Parse input"""
    data = [line.split(" ") for line in puzzle_input.split("\n")]

    root = Folder(ROOT_MARKER)

    for line in data:
        if line[0] == INSTRUCTION_MARKER:
            if line[1] == CD_MARKER:
                # Changing folder
                if line[2] == ROOT_MARKER:
                    # we are at root
                    current_folder = root
                elif line[2] == CD_UP_MARKER:
                    if current_folder.parent:
                        current_folder = current_folder.parent
                    else:
                        current_folder = root

                else:
                    # change folder
                    change_folder = Folder(line[2])
                    current_folder.add_child(change_folder)
                    current_folder = change_folder
        else:
            # we are listing the current folder
            if line[0] != DIR_MARKER:
                new_file = File(name=line[1], size=int(line[0]), parent=current_folder)
                current_folder.add_child(new_file)  
    
    return root


def part1(data):
    return [folder.get_size(100000) for folder in data.children if isinstance(folder,Folder) and folder.marked_for_deletion]


def part2(data):
    return data


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
