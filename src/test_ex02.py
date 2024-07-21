def my_sum(a, b):
    """Return the sum of two integers"""
    if not all(isinstance(arg, int) for arg in (a, b)):
        raise ValueError("All arguments must be integers")

    return a + b


def test_my_sum():
    """Tests the my_sum function"""
    # Avoid importing test module during normal operation
    import sys

    import pytest

    # Happy path
    assert my_sum(2, 3) == 5
    assert my_sum(-2, -3) == -5
    assert my_sum(0, 0) == 0
    # Largest and smallest integers
    assert my_sum(sys.maxsize, -sys.maxsize - 1) == -1
    # Negative cases
    with pytest.raises(ValueError):
        my_sum("2", 3)  # Non-integer input
    with pytest.raises(ValueError):
        my_sum(2, 3.5)  # Non-integer input
    with pytest.raises(ValueError):
        my_sum(None, 3)  # None input
    with pytest.raises(ValueError):
        my_sum(2, None)  # None input
