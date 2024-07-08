# Exercise 8: Price with Tax


# Define tax rules
TAX_THRESHOLD = 100  # Minimum price for tax to be applied
TAX_RATE = 0.25


def add_tax(price):
    """Calculate the full price of an item including tax."""
    if not isinstance(price, int):
        raise TypeError("Argument must be an integer")
    if price < 0:
        raise ValueError("Value must be non-negative")
    tax = max(0, (price - TAX_THRESHOLD) * TAX_RATE)

    return price + tax


# Print example outputs
print(add_tax(120))
print(add_tax(425))


def test_add_tax():
    """Test the add_tax function."""
    import sys

    import pytest

    # Happy path
    assert add_tax(150) == 162.5  # Above tax threshold

    # Edge cases
    assert add_tax(0) == 0.0  # Zero price
    assert add_tax(TAX_THRESHOLD) == float(TAX_THRESHOLD)  # At tax threshold
    assert add_tax(TAX_THRESHOLD - 1) == float(
        TAX_THRESHOLD - 1
    )  # Below tax threshold
    assert add_tax(sys.maxsize) == pytest.approx(
        sys.maxsize + ((sys.maxsize - TAX_THRESHOLD) * TAX_RATE)
    )  # Very large price

    # Negative tests
    with pytest.raises(TypeError):
        add_tax(100.5)
    with pytest.raises(TypeError):
        add_tax("100")
    with pytest.raises(ValueError):
        add_tax(-1)
