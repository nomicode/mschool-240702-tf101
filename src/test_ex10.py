# Exercise 10: Middle digit


def middle_digit(num):
    """Return the middle digit of a three digit number."""
    if not isinstance(num, int):
        raise TypeError("Argument must be an integer")
    if not 100 <= num <= 999:
        raise ValueError("Value must be a three digit number")

    return int(str(num)[1])


# Print example outputs
print(middle_digit(234))
print(middle_digit(902))


def test_middle_digit():
    """Test the middle_digit function."""
    import pytest

    # Happy path
    assert middle_digit(123) == 2
    assert middle_digit(456) == 5
    assert middle_digit(789) == 8

    # Edge cases
    assert middle_digit(100) == 0
    assert middle_digit(999) == 9

    # Negative tests
    with pytest.raises(TypeError):
        middle_digit(100.0)
    with pytest.raises(TypeError):
        middle_digit("100")
    with pytest.raises(ValueError):
        middle_digit(0)
        middle_digit(000)  # Python syntax quirk (equals 0)
        middle_digit(99)  # One digit too small
        middle_digit(1000)  # One digit too large
        middle_digit(-100)  # Negative three digit number
