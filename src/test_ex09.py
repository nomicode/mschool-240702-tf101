# Exercise 9: Distance between points


def euclidean_distance(x1, y1, x2, y2):
<<<<<<< HEAD
<<<<<<< HEAD:src/test_ex09.py
    pass
=======
=======
    """Calculate the Euclidean distance between two points."""
    if not all(isinstance(arg, float) for arg in (x1, y1, x2, y2)):
        raise ValueError("All arguments must be floats")
>>>>>>> b987e6e (fixup09)
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
>>>>>>> a3cda26 (Add solution and tests for exercise 9):course/ms/csec/tf/101/1/src/test_ex09.py


# Print example output
print(euclidean_distance(1.5, 3.0, 4.0, 8.0))


def test_euclidean_distance():
    """Test the euclidean_distance function."""
    # Modules only used for testing
    import sys

    import pytest

    # Happy path tests
    assert dist(0.0, 0.0, 3.0, 4.0) == pytest.approx(
        5.0
    )  # Classic 3-4-5 triangle
    assert dist(1.0, 1.0, 4.0, 5.0) == pytest.approx(
        5.0
    )  # Shifted 3-4-5 triangle
    assert dist(0.0, 0.0, 0.0, 0.0) == pytest.approx(0.0)  # Same point
    assert dist(-1.0, -1.0, 1.0, 1.0) == pytest.approx(
        2.8284271247461903
    )  # Negative coordinates

    # Edge cases
    assert dist(0.0, 0.0, 3.0, 0.0) == pytest.approx(3.0)  # Horizontal line
    assert dist(0.0, 0.0, 0.0, 3.0) == pytest.approx(3.0)  # Vertical line
    assert dist(0.0, 0.0, 3.0, 3.0) == pytest.approx(
        4.242640687119285
    )  # Diagonal line
    assert dist(
        0.0, 0.0, float(sys.maxsize), float(sys.maxsize)
    ) == pytest.approx(
        1.3043817825332783e19
    )  # Very large coordinates
    assert dist(
        0.0, 0.0, float(sys.maxsize), float(-sys.maxsize)
    ) == pytest.approx(
        1.3043817825332783e19
    )  # Very large negative coordinates

    # Negative tests
    with pytest.raises(ValueError):
        # x1 is an integer instead of float
        dist(0, 0.0, 3.0, 4.0)
        # y1 is a string instead of float
        dist(0.0, "0.0", 3.0, 4.0)
        # x2 a tuple instead of float
        dist(0.0, 0.0, (3.0), 4.0)
        # y2 is None instead of float
        dist(0.0, 0.0, 3.0, None)
