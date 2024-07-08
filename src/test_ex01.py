# Define the current year for this exercise (in a normal application, the value
# would probably be set at runtime instead of being hardcoded)
current_year = 2023


def age(birth_year):
    """Guess the age of a person born in the given year."""
    if not isinstance(birth_year, int):
        raise TypeError("Argument must be an integer")
    if birth_year > current_year:
        raise ValueError("Value cannot be greater than the current year")
    approx_age = current_year - birth_year
    born_str = f"You were born in {birth_year}"
    age_str = f"so you are about {approx_age} years old."

    return f"{born_str}, {age_str}"


# Print example output
text = age(1983)
print(text)


def test_age():
    """Test the age function"""
    import pytest

    # Aliases for readability
    max_year = current_year
    prefix = "You were born in "
    infix = ", so you are about "
    suffix = " years old."

    # Happy path
    assert age(2000) == f"{prefix}2000{infix}23{suffix}"

    # Edge cases
    assert age(0) == f"{prefix}0{infix}{max_year}{suffix}"  # Lower bound
    # Upper bound
    assert age(max_year) == f"{prefix}{max_year}{infix}0{suffix}"

    # Negative tests
    with pytest.raises(TypeError):
        age(2000.0)
    with pytest.raises(TypeError):
        age("2000")
    with pytest.raises(ValueError):
        # We don't allow time travel
        age(max_year + 1)
