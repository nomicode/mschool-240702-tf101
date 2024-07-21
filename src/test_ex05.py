<<<<<<< HEAD:src/test_ex05.py
"""Exercise 5: Title Creator"""


def title_creator(title, char, times):
    pass


def test_title_creator():
    pass
=======
# Exercise 5: Title Creator


def title_creator(title, char, times):
    """Format a title using char repeated multiple times on each side."""
    if not isinstance(title, str):
        raise ValueError("Argument must be an string")
    if not isinstance(char, str):
        raise ValueError("Argument must be an string")
    if not isinstance(times, int) or times < 0:
        raise ValueError("Argument must be a positive integer")
    affix = char * times
    return f"{affix}{title}{affix}"


def test_title_creator():
    """Test the title_creator function."""
    # Module only used for testing
    import pytest

    # Happy path
    assert title_creator("Title", "=", 1) == "=Title="
    assert title_creator("Title", "=", 2) == "==Title=="

    # Edge cases
    assert title_creator("Title", "=", 0) == "Title"  # Zero times
    assert title_creator("Title", "", 1) == "Title"  # Empty char
    assert title_creator("", "=", 1) == "=="  # Empty title
    assert title_creator("", "", 1) == ""  # Empty title and char

    # Negative tests
    with pytest.raises(ValueError):
        # 1st argument not a string
        title_creator(123, "=", 1)
        # 2nd argument not a string
        title_creator("Title", 123, 1)
        # 3rd argument not an integer
        title_creator("Title", "=", 1.0)
        title_creator("Title", "=", "1")
        title_creator("Title", "=", None)
>>>>>>> 5282ae5 (Add solution and tests for exercise 5):course/ms/csec/tf/101/1/src/test_ex05.py


# Print example output
print(title_creator("Welcome to Masterschool", "=", 5))
