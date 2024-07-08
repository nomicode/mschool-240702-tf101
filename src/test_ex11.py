# Exercise 11: Reverse numbers


def reverse_number(number):
    """Reverse a five digit number."""
    if not isinstance(number, int):
        raise TypeError("Argument must be an integer")
    if not 10000 <= number <= 99999:
        raise ValueError("Value must be a five digit number")

    return int(str(number)[::-1])


# Print example outputs
print(reverse_number(12345))


def test_reverse_number():
    """Test the reverse_number function."""
    import pytest

    # Happy path
    assert reverse_number(12345) == 54321
    assert reverse_number(67890) == 9876  # Leading zeros are removed

    # Edge cases
    assert reverse_number(10000) == 1
    assert reverse_number(99999) == 99999

    # Negative tests
    with pytest.raises(TypeError):
        reverse_number(10000.0)
    with pytest.raises(TypeError):
        reverse_number("10000")
    with pytest.raises(ValueError):
        reverse_number(0)
        reverse_number(00000)  # Python syntax quirk (equals 0)
        reverse_number(9999)  # One digit too small
        reverse_number(100000)  # One digit too large
        reverse_number(-10000)  # Negative five digit number
