# Exercise 5: Title Creator


def title_creator(title, char, times):
    """Format a title using a char repeated multiple times on either side."""
    if not all(isinstance(arg, str) for arg in (title, char)):
        raise TypeError("Arguments must be strings")
    if not isinstance(times, int):
        raise TypeError("Argument must be an string")
    if times < 0:
        raise ValueError("Value must be non-negative")
    affix = char * times

    return f"{affix}{title}{affix}"


# Print example output
print(title_creator("Welcome to Masterschool", "=", 5))


def test_title_creator():
    """Test the title_creator function."""
    import pytest

    # Happy path
    assert title_creator("Title", "=", 1) == "=Title="
    assert title_creator("Title", "=", 2) == "==Title=="

    # Edge cases
    assert title_creator("Title", "=", 0) == "Title"  # Zero times
    assert title_creator("Title", "", 1) == "Title"  # Empty char
    assert title_creator("", "=", 1) == "=="  # Empty title
    assert title_creator("", "", 1) == ""  # Empty title and char

    # Note: Testing the limits of the integer value would be too complex for
    # this exercise. We would need to consider factors like the bit size of
    # Unicode code points, system architecture, available memory, and other
    # factors.

    # Negative tests
    with pytest.raises(TypeError):
        title_creator(None, "=", 1)
    with pytest.raises(TypeError):
        title_creator("Title", None, 1)
    with pytest.raises(TypeError):
        title_creator("Title", "=", 1.0)
    with pytest.raises(TypeError):
        title_creator("Title", "=", "1")
