import pathlib

import day1 as aoc
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    print(f'Looking for test data in {PUZZLE_DIR}')
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc.parse(puzzle_input)


@pytest.fixture
def example2():
    print(f'Looking for test data in {PUZZLE_DIR}')
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == ['1000', '2000', '3000', '', '4000', '', '5000', '6000', '', '7000', '8000', '9000', '', '10000']


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 24000


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc.part2(example1) == 45000


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc.part2(example2) == ...
