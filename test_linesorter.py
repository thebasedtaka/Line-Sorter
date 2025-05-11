import pytest
from linesorter import sort_file, print_file

TEST_INPUT_FILE = "ShortStory.txt"


def test_sort_file_removes_empty_lines(tmp_path):
    """Test if empty lines are removed."""
    test_file = tmp_path / TEST_INPUT_FILE
    test_file.write_text("A\n\nB\n  \nC")
    result = sort_file(test_file)
    assert result == ["A", "B", "C"]

def test_sort_file_removes_dash_lines(tmp_path):
    """Test if lines with only dashes are removed."""
    test_file = tmp_path / TEST_INPUT_FILE
    test_file.write_text("Apple\n---\nBanana\n----")
    result = sort_file(test_file)
    assert result == ["Apple", "Banana"]

def test_sort_file_sorts_alphabetically(tmp_path):
    """Test if lines are sorted case-insensitively."""
    test_file = tmp_path / TEST_INPUT_FILE
    test_file.write_text("banana\nApple\nCherry")
    result = sort_file(test_file)
    assert result == ["Apple", "banana", "Cherry"]