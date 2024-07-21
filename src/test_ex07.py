# Exercise 7: Percent calculation

# Define the precision of the percentage in decimal places
PRECISION = 1


def percent(num1, num2):
<<<<<<< HEAD
<<<<<<< HEAD:src/test_ex07.py
    # Your code here
    pass
=======
    return (num1 / num2) * 100
>>>>>>> 31bf828 (Add solution and tests for exercise 7):course/ms/csec/tf/101/1/src/test_ex07.py
=======
    """Calculate the percentage of one number relative to another."""
    if not all(isinstance(arg, (int, float)) for arg in (num1, num2)):
        raise ValueError("All arguments must be integers or floats")
    # Avoid division by zero
    if num2 == 0:
        raise ValueError("The second argument cannot not be zero.")
    # Round to the specified precision
    return round((num1 / num2) * 100, PRECISION)
>>>>>>> c0de9b2 (fixup07)


def test_percent():
    """Test the percent function."""
    # Module only used for testing
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
    # Max integer is 100% of itself
    assert percent(sys.maxsize, sys.maxsize) == 100

    # Error tests
    with pytest.raises(ValueError):
        percent(1, 0)  # Would result in division by zero
        percent("1", 100)  # Not a number
        percent(100, "1")  # Not a number
        percent(None, 100)  # None
        percent(100, None)  # None


# Print example outputs
print(percent(155, 500))
print(percent(250, 125))
