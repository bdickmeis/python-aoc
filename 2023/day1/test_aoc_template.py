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


# @pytest.mark.skip(reason="Not implemented")
def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]


def test_parse_example2(example2):
    """Test that input is parsed properly"""
    assert example2 == [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen",
    ]


# @pytest.mark.skip(reason="Not implemented")
def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc.part1(example1) == 142


# @pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc.part2(example1) == 142


# @pytest.mark.skip(reason="Not implemented")
def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc.part2(example2) == 281


test_data = [
    ("6fourzpjthmkrkvqkvvp", "64zpjthmkrkvqkvvp", 64),
    ("eightthsix1", "8th61", 81),
    ("8nvrmzfs46","8nvrmzfs46",86),
    ("vnrnkfp6","vnrnkfp6",66),
]


@pytest.mark.parametrize("test_input,processed,expected", test_data)
def test_replace_digit_words(test_input, processed, expected):
    assert aoc.replace_digit_words(test_input) == processed
    assert aoc.get_calibration_value(processed) == expected
