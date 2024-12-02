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

def test_parse_rgb():
    assert aoc.parse_rgb("3 blue, 4 red") == (4,0,3)


def test_is_game_possible():
    assert aoc.is_game_possible([(14, 0, 3), (1, 2, 6), (0, 2, 0)]) == False


def test_get_power_set():
    assert aoc.get_power_set([(4, 0, 3), (1, 2, 6), (0, 2, 0)]) == 48

@pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == {1: [(4, 0, 3), (1, 2, 6), (0, 2, 0)]}


#@pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 8


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc.part2(example1) == ...


@pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc.part2(example2) == ...
