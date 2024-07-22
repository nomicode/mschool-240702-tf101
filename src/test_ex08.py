# Exercise 8: Price with Tax


# Define tax rules
TAX_THRESHOLD = 100  # Minimum price for tax to be applied
TAX_RATE = 0.25

# The exercise requires the function to return a float, but the first example
# is given as:
#
#   >> print(add_tax(120))
#   125
#
# A float would print as `125.0`, suggesting that `125` is an integer.
#
# I am sure this is just a typo, but to have a little fun, and to resolve this
# ambiguity in a way that reproduces the examples given, we can subclass the
# built-in float.


class IntFloat(float):
    """Simultaneously a float and a localized currency string.

    By way of analogy to quantum physics and wave-particle duality, this class
    behaves like a float until you "look at it" (print it, etc.), at which
    point it will collapse into an int (if it has no fractional part).
    """

    def __new__(cls, value):
        """Initialize a new CurrencyFloat instance."""
        return super().__new__(cls, value)

    def __str__(self):
        """Cast the float to a localized currency string."""
        return f"{int(self)}" if self.is_integer() else str(float(self))

    def __repr__(self):
        """Return a string representation of the object."""
        return self.__str__()


def add_tax(price):
    """Calculate the full price of an item including tax."""
    if not isinstance(price, int):
        raise TypeError("Argument must be an integer")
    if price < 0:
        raise ValueError("Value must be non-negative")

    return IntFloat(price + max(0, (price - TAX_THRESHOLD) * TAX_RATE))


# Print example outputs
print(add_tax(120))
print(add_tax(425))


def test_decimal_float():
    """Test the CurrencyFloat class."""
    import pytest

    def _assert_decimal(value, expected):
        """Assert that the value prints as expected."""
        result = IntFloat(value)
        assert str(result) == expected
        assert repr(result) == expected

    def _assert_float(value1, value2, operation, expected):
        """Assert the result of a float operation."""
        result = operation(IntFloat(value1), IntFloat(value2))
        assert result == pytest.approx(expected)

    # Happy path
    _assert_decimal(1, "1")  # No decimal places (like an int)
    _assert_decimal(1.0, "1")  # No decimal places (like an int)
    _assert_decimal(1.00, "1")  # No decimal places (like an int)
    _assert_float(5, 3, lambda x, y: x + y, 5 + 3)  # Addition
    _assert_float(5, 3, lambda x, y: x * y, 5 * 3)  # Multiplication

    # Edge cases
    _assert_decimal("0", "0")  # Initialized as a string
    _assert_decimal(-1, "-1")  # Minus with no decimal places (like an int)
    _assert_decimal(-1.1, "-1.1")  # No decimal places padding
    _assert_decimal(-1.11, "-1.11")  # No modification
    _assert_decimal(1.015, "1.015")  # No bankers' rounding to cents
    _assert_decimal(1.025, "1.025")  # No bankers' rounding to cents
    _assert_float(3, 5, lambda x, y: x - y, 3 - 5)  # Subtraction (negative)
    _assert_float(5, 3, lambda x, y: x / y, 5 / 3)  # Division (irrational)

    # Negative tests
    with pytest.raises(TypeError):
        IntFloat(None)


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
