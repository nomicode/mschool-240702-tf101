# Exercise 8: Price with Tax


TAX_THRESHOLD = 100
TAX_RATE = 0.25


def add_tax(price):
<<<<<<< HEAD
<<<<<<< HEAD:src/test_ex08.py
    pass
=======
    return price * 1.07
>>>>>>> f5c2a1b (Add solution and tests for exercise 8):course/ms/csec/tf/101/1/src/test_ex08.py
=======
    """Calculate the full price of an item including tax."""
    if not isinstance(price, int) or price < 0:
        raise ValueError("Argument must be a non-negative integer")
    tax = (price - TAX_THRESHOLD) * TAX_RATE
    return price + tax if tax > 0 else price
>>>>>>> b0449e6 (fixup08)


def test_add_tax():
    """Test the add_tax function."""
    # Module only used for testing
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
    with pytest.raises(ValueError):
        add_tax(-1)  # Negative price
        add_tax("100")  # Test string input
        add_tax(100.5)  # Test float input


# Print example outputs
print(add_tax(120))
print(add_tax(425))
