import pathlib

import aoc_template as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)


#@pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
    """Test that input is parsed properly"""

    assert example1[0] == ['4','6','7','.','.','1','1','4','.','.']
    assert example1[1] == ['.','.','.','*','.','.','.','.','.','.']
    assert example1[2] == ['.','.','3','5','.','.','6','3','3','.']
    assert example1[3] == ['.','.','.','.','.','.','#','.','.','.']
    assert example1[4] == ['6','1','7','*','.','.','.','.','.','.']
    assert example1[5] == ['.','.','.','.','.','+','.','5','8','.']
    assert example1[6] == ['.','.','5','9','2','.','.','.','.','.']
    assert example1[7] == ['.','.','.','.','.','.','7','5','5','.']
    assert example1[8] == ['.','.','.','$','.','*','.','.','.','.']
    assert example1[9] == ['.','6','6','4','.','5','9','8','.','.']

def test_detect_symbols(example1):
    expected_symbols = [(1, 3), (3, 6), (4, 3), (5, 5), (8, 3), (8, 5)]
    assert aoc.detect_symbols(example1) == expected_symbols

def test_adj_digits(example1):
    expected_symbols = [(1, 3), (3, 6), (4, 3), (5, 5), (8, 3), (8, 5)]
    expected_adj_digits = [(0, 2), (2, 2), (2, 3), (2, 6), (2, 7), (4, 2), (6, 4), (7, 6), (9, 2), (9, 3), (9, 5), (9, 6)]
    assert aoc.detect_symbols(example1) == expected_symbols
    assert aoc.find_adjacent_digits(example1,expected_symbols) == expected_adj_digits

def test_remove_double_detection():
    assert aoc.remove_double_detection([(0, 2), (2, 2), (2, 3), (2, 6), (2, 7), (4, 2), (6, 4), (7, 6), (9, 2), (9, 3), (9, 5), (9, 6)]) == ...

@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 4361


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc.part2(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc.part2(example2) == ...
