# Exercise 1: Print age


def my_sum(a, b):
    """Calculate the sum of two integers."""
    if not all(isinstance(arg, int) for arg in (a, b)):
        raise ValueError("All arguments must be integers")

    return a + b


def test_my_sum():
    """Test the my_sum function."""
    # Modules only used for testing
    import sys

    import pytest

    # Happy path
    assert my_sum(2, 3) == 5
    assert my_sum(-2, -3) == -5
    assert my_sum(0, 0) == 0

    # Edge cases
    assert my_sum(sys.maxsize, -sys.maxsize - 1) == -1  # Very large numbers

    # Negative cases
    with pytest.raises(ValueError):
        my_sum("1", 1)  # String input
        my_sum(1, 1.0)  # Float input
        my_sum(None, 1)  # None input
        my_sum(1, None)  # None input
