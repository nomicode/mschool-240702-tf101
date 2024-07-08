# Exercise 4: Currency Convertor

EXCHANGE_RATE = 7.15


def usd_to_yuan(dollars):
    """Convert USD to Chinese Yuan."""
    if not isinstance(dollars, int):
        raise TypeError("Argument must be an integer")

    return dollars * EXCHANGE_RATE


# Print example output
print(usd_to_yuan(10))


def test_usd_to_yuan():
    """Test the usd_to_yuan function."""
    import sys

    import pytest

    # Happy path
    assert usd_to_yuan(1) == 7.15  # Positive integer
    assert usd_to_yuan(-1) == -7.15  # Negative integer

    # Edge cases
    assert usd_to_yuan(0) == 0  # Zero
    assert usd_to_yuan(-0) == 0  # Negative zero
    assert usd_to_yuan(sys.maxsize) == pytest.approx(
        sys.maxsize * EXCHANGE_RATE
    )  # Very large number

    # Negative tests
    with pytest.raises(TypeError):
        usd_to_yuan(1.0)
    with pytest.raises(TypeError):
        usd_to_yuan("1")
