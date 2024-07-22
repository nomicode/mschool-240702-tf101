# Hard code the current year for this exercise
current_year = 2023


def age(birth_year):
    """Guess the age of a person born in the given year."""
    if not isinstance(birth_year, int) or birth_year < 0:
        raise ValueError("Argument must be a positive integer")
    if birth_year > current_year:
        raise ValueError("Year cannot be in the future")
    age_guess = current_year - birth_year
    # Split string over two lines for readability
    born_str = f"You were born in {birth_year}"
    age_str = f"so you are about {age_guess} years old."
    return f"{born_str}, {age_str}"


# Print example output
text = age(1983)
print(text)


def test_ageh():
    """Test the age function"""
    # Module imported here because it is only needed for testing
    import pytest

    # Happy path
    assert (
        age(2000)
        == "You were born in 2000, " + "so you are about 23 years old."
    )

    # Edge cases
    assert (
        age(0) == "You were born in 0, " + "so you are about 2023 years old."
    )  # Lower bound
    assert (
        age(2023)
        == "You were born in 2023, " + "so you are about 0 years old."
    )  # Upper bound

    # Negative tests
    with pytest.raises(ValueError):
        age(-1)  # Negative year
        age(current_year + 1)  # Future year
        # Non-integer inputs
        age(2000.0)  # Float
        age("2000")  # String
        age([2000])  # Tuple
        age(None)  # None
