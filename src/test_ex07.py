# Exercise 7: Percent calculation

# Define the precision of the percentage in decimal places
PRECISION = 1


def percent(num1, num2):
    """Calculate the percentage of one number relative to another."""
    if not all(isinstance(arg, int) for arg in (num1, num2)):
        raise TypeError("Arguments must be integers")
    if num2 == 0:
        raise ZeroDivisionError("Value cannot not be zero")

    return round((num1 / num2) * 100, PRECISION)


# Print example outputs
print(percent(155, 500))
print(percent(250, 125))


def test_percent():
    """Test the percent function."""
    import sys

    import pytest

    # Happy path tests
    assert percent(1, 10) == 10.0  # Positive
    assert percent(10, 1) == 1000.0  # Positive
    assert percent(-1, 10) == -10.0  # Negative
    assert percent(10, -1) == -1000.0  # Negative

    # Edge cases
    assert percent(0, 1) == 0.0  # Any percentage of zero is zero
    assert percent(1, 1) == 100.0  # 100% of itself
    assert percent(1, 7) == 14.3  # Non-integer percentage
    assert percent(sys.maxsize, 1) == pytest.approx(
        sys.maxsize * 100
    )  # Multiplication of very large number
    assert percent(1, sys.maxsize) == pytest.approx(
        float((1 / sys.maxsize) * 100)
    )  # Division of very large number
    assert percent(sys.maxsize, sys.maxsize) == 100  # Still 100% of itself

    # Error tests
    with pytest.raises(TypeError):
        percent("1", 100)
    with pytest.raises(TypeError):
        percent(100, 1.0)
    with pytest.raises(ZeroDivisionError):
        percent(1, 0)
