# Exercise 4: Currency Convertor

EXCHANGE_RATE = 7.15


def usd_to_yuan(dollars):
<<<<<<< HEAD
<<<<<<< HEAD:src/test_ex04.py
    """Converts USD to Chinese Yuan.

    Args:
        dollars (int): Amount in USD
    Raises:
        ValueError: If the input is not an integer
    Returns:
        float: Amount in Chinese Yuan
    """
=======
    """Converts USD to Chinese Yuan."""
>>>>>>> 9833c82 (Add solution and tests for exercise 4):course/ms/csec/tf/101/1/src/test_ex04.py
=======
    """Convert USD to Chinese Yuan."""
>>>>>>> 0332918 (fixup04)
    if not isinstance(dollars, int):
        raise ValueError("Argument must be an integer")
    return dollars * EXCHANGE_RATE


# Print example output
print(usd_to_yuan(10))


def test_usd_to_yuan():
<<<<<<< HEAD
    """Test case for usd_to_yuan function."""
    # Avoid importing test modules during normal operation
<<<<<<< HEAD:src/test_ex04.py
    # pylint: disable=import-outside-toplevel
=======
>>>>>>> 9833c82 (Add solution and tests for exercise 4):course/ms/csec/tf/101/1/src/test_ex04.py
    import math
=======
    """Test the usd_to_yuan function."""
    # Modules only used for testing
>>>>>>> 0332918 (fixup04)
    import sys

    import pytest

<<<<<<< HEAD:src/test_ex04.py
    # trunk-ignore-all(bandit/B101)
=======
>>>>>>> 9833c82 (Add solution and tests for exercise 4):course/ms/csec/tf/101/1/src/test_ex04.py
    # Happy path
    assert usd_to_yuan(1) == 7.15  # Positive integer
    assert usd_to_yuan(-1) == -7.15  # Negative integer

    # Edge cases
    assert usd_to_yuan(0) == 0  # Zero
    assert usd_to_yuan(-0) == 0  # Negative zero
<<<<<<< HEAD
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
<<<<<<< HEAD:src/test_ex04.py
    with pytest.raises(ValueError):  # String input
        usd_to_yuan("one")
=======
>>>>>>> 9833c82 (Add solution and tests for exercise 4):course/ms/csec/tf/101/1/src/test_ex04.py
    with pytest.raises(ValueError):  # None input
        usd_to_yuan(None)
=======
    assert usd_to_yuan(sys.maxsize) == pytest.approx(
        sys.maxsize * EXCHANGE_RATE
    )  # Very large number
>>>>>>> 0332918 (fixup04)

    # Negative tests
    with pytest.raises(ValueError):
        usd_to_yuan(1.0)  # Float
    with pytest.raises(ValueError):
        usd_to_yuan("1")  # String
    with pytest.raises(ValueError):
        usd_to_yuan(None)  # None
