# Exercise 4: Currency Convertor

EXCHANGE_RATE = 7.15


def usd_to_yuan(dollars):
    """Converts USD to Chinese Yuan.

    Args:
        dollars (int): Amount in USD
    Raises:
        ValueError: If the input is not an integer
    Returns:
        float: Amount in Chinese Yuan
    """
    if not isinstance(dollars, int):
        raise ValueError("Argument must be an integer")
    return dollars * EXCHANGE_RATE


def test_usd_to_yuan():
    """Test case for usd_to_yuan function."""
    # Avoid importing test modules during normal operation
    # pylint: disable=import-outside-toplevel
    import math
    import sys

    import pytest

    # trunk-ignore-all(bandit/B101)
    # Happy path
    assert usd_to_yuan(1) == 7.15  # Positive integer
    assert usd_to_yuan(-1) == -7.15  # Negative integer
    # Edge cases
    assert usd_to_yuan(0) == 0  # Zero
    assert usd_to_yuan(-0) == 0  # Negative zero
    assert math.isclose(
        usd_to_yuan(sys.maxsize),
        sys.maxsize * EXCHANGE_RATE,
        rel_tol=1e-9,
        abs_tol=1e-9,
    )  # Max integer
    # Negative cases
    with pytest.raises(ValueError):  # Float input
        usd_to_yuan(1.0)
    with pytest.raises(ValueError):  # String input
        usd_to_yuan("1")
    with pytest.raises(ValueError):  # String input
        usd_to_yuan("one")
    with pytest.raises(ValueError):  # None input
        usd_to_yuan(None)


# Print example output
print(usd_to_yuan(10))
