<<<<<<< HEAD
<<<<<<< HEAD:src/test_ex06.py
"""Exercise 6: Coffee Cost"""


def coffee_calculator(small, medium, large):
    pass


def test_coffee_calculator():
    pass
=======
# Exercise 6: Coffee Cost"
=======
# Exercise 6: Coffee Cost
>>>>>>> f8fda0b (fixup06)

SMALL_COST = 2
MEDIUM_COST = 3
LARGE_COST = 4


def coffee_calculator(small, medium, large):
    """Calculate the total cost of a coffee order."""
    if not all(
        isinstance(arg, int) and arg >= 0 for arg in (small, medium, large)
    ):
        raise ValueError("All arguments must be positive integers")
    return (small * SMALL_COST) + (medium * MEDIUM_COST) + (large * LARGE_COST)


def test_coffee_calculator():
    """Test the coffee_calculator function."""
    # Modules only used for testing
    import sys

    import pytest

    # Happy path
    assert coffee_calculator(1, 1, 1) == 9  # Single multiples
    assert coffee_calculator(2, 2, 2) == 18  # Multiple multiples

    # Edge cases
    assert coffee_calculator(0, 1, 1) == 7  # 1st argument zero
    assert coffee_calculator(1, 0, 1) == 6  # 2nd argument zero
    assert coffee_calculator(1, 1, 0) == 5  # 3rd argument zero
    assert coffee_calculator(0, 0, 0) == 0  # All arguments zero
    assert coffee_calculator(
        sys.maxsize, sys.maxsize, sys.maxsize
    ) == sys.maxsize * (
        SMALL_COST + MEDIUM_COST + LARGE_COST
    )  # Very large numbers

    # Negative tests
    def _test_args(good_value, bad_value):
        """Test arguments with good and bad values."""
        coffee_calculator(bad_value, good_value, good_value)
        coffee_calculator(good_value, bad_value, good_value)
        coffee_calculator(good_value, good_value, bad_value)

    with pytest.raises(ValueError):
        _test_args(1, -1)  # Negative integer
        _test_args("1", -1)  # String
        _test_args(1.0, -1)  # Float
        _test_args(None, -1)  # None
>>>>>>> 05032b3 (Add solution and tests for exercise 6):course/ms/csec/tf/101/1/src/test_ex06.py


# Print example output
print(coffee_calculator(2, 10, 1))
