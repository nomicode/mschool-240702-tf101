# Exercise 6: Coffee Cost

# Define prices for each size of coffee
SMALL_COST = 2
MEDIUM_COST = 3
LARGE_COST = 4


def coffee_calculator(small, medium, large):
    """Calculate the total cost of a coffee order."""
    if not all(isinstance(arg, int) for arg in (small, medium, large)):
        raise TypeError("Arguments must be integers")
    if any(arg < 0 for arg in (small, medium, large)):
        raise ValueError("Values must be non-negative")

    return (small * SMALL_COST) + (medium * MEDIUM_COST) + (large * LARGE_COST)


# Print example output
print(coffee_calculator(2, 10, 1))


def test_coffee_calculator():
    """Test the coffee_calculator function."""
    import sys

    import pytest

    # Happy path
    assert coffee_calculator(1, 1, 1) == 9  # Single multiples
    assert coffee_calculator(2, 2, 2) == 18  # Multiple multiples

    # Edge cases
    assert coffee_calculator(0, 1, 1) == 7  # 1st argument zero
    assert coffee_calculator(1, 0, 1) == 6  # 2nd argument zero
    assert coffee_calculator(1, 1, 0) == 5  # 3rd argument zero
    assert coffee_calculator(0, 0, 0) == 0  # All arguments zero
    assert coffee_calculator(
        sys.maxsize, sys.maxsize, sys.maxsize
    ) == sys.maxsize * (
        SMALL_COST + MEDIUM_COST + LARGE_COST
    )  # Very large numbers

    # Negative tests
    with pytest.raises(TypeError):
        coffee_calculator(1.0, 1, 1)
    with pytest.raises(TypeError):
        coffee_calculator(1, "1", 1)
    with pytest.raises(TypeError):
        coffee_calculator(1, "1", None)
    with pytest.raises(ValueError):
        coffee_calculator(-1, 1, 1)
    with pytest.raises(ValueError):
        coffee_calculator(1, -1, 1)
    with pytest.raises(ValueError):
        coffee_calculator(1, 1, -1)
