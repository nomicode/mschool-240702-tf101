# Exercise 9: Distance between points


# This exercise specifies that all arguments are floats. However, if we test
# for that concretely, we fail the tests. As a solution we have to loosen up
# our type checking, and check for numeric values instead.


def euclidean_distance(x1, y1, x2, y2):
    """Calculate the Euclidean distance between two points."""
    # Disabled if we expect ints
    # if not all(isinstance(arg, float) for arg in (x1, y1, x2, y2)):
    #    raise ValueError("All arguments must be floats")
    if not all(isinstance(arg, (int, float)) for arg in (x1, y1, x2, y2)):
        raise ValueError("All arguments must be numeric")

    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


# Print example output
print(euclidean_distance(1.5, 3.0, 4.0, 8.0))


def test_euclidean_distance():
    """Test the euclidean_distance function."""
    import sys

    import pytest

    # Aliases for readability
    ed = euclidean_distance
    approx = pytest.approx

    # Happy path tests
    assert ed(0.0, 0.0, 3.0, 4.0) == 5.0  # Classic 3-4-5 triangle
    assert ed(1.0, 1.0, 4.0, 5.0) == 5.0  # Shifted 3-4-5 triangle
    assert ed(0.0, 0.0, 0.0, 0.0) == 0.0  # Same point
    assert ed(-1.0, -1.0, 1.0, 1.0) == approx(
        2.8284271247461903
    )  # Negative coordinates

    # Edge cases
    assert ed(0.0, 0.0, 3.0, 0.0) == 3.0  # Horizontal line
    assert ed(0.0, 0.0, 0.0, 3.0) == 3.0  # Vertical line
    assert ed(0.0, 0.0, 3.0, 3.0) == approx(4.242640687119285)  # Diagonal line
    assert ed(0.0, 0.0, float(sys.maxsize), float(sys.maxsize)) == approx(
        1.3043817825332783e19
    )  # Maximum integer coordinates
    assert ed(0.0, 0.0, float(sys.maxsize), float(-sys.maxsize)) == approx(
        1.3043817825332783e19
    )  # Negative maximum integer coordinates

    # Negative tests
    # with pytest.raises(ValueError):  # Disabled if we expect ints
    #     ed(0, 0.0, 0.0, 0.0)
    with pytest.raises(ValueError):
        ed(0.0, "0.0", 0.0, 0.0)
    with pytest.raises(ValueError):
        ed(0.0, 0.0, None, 0.0)
    with pytest.raises(ValueError):
        ed(0.0, 0.0, 0.0, [1.0])
    with pytest.raises(OverflowError):
        ed(float(sys.float_info.max), float(sys.float_info.max), 0.0, 0.0)
