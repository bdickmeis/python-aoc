import pathlib

import aoc_template as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text()
    return aoc.parse_input(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text()
    return aoc.parse_input(puzzle_input)




def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == {'stack': [['Z','N'],['M','C','D'],['P']], 'movements': [(1, 1, 0), (3, 0, 2), (2, 1, 0), (1, 0, 1)]}



def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == "CMZ"


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc.part2(example1) == "MCD"


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc.part2(example2) == ...
