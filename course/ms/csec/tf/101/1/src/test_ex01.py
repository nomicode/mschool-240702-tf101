# Hard code the current year for this exercise
current_year = 2023


def fmt_text(birth_year, age_guess):
    """Format the age guess text for a given birth year"""
    # Split string over two lines for readability
    born_str = f"You were born in {birth_year}"
    age_str = f"so you are about {age_guess} years old."
    return f"{born_str}, {age_str}"


def age(birth_year):
    """Guess the age of a person born in the given year"""
    if not isinstance(birth_year, int):
        raise ValueError("Year must be an integer")

    age_guess = current_year - birth_year
    if age_guess < 0:
        raise ValueError("Age cannot be negative")

    return fmt_text(birth_year, age_guess)


def test_age():
    """Tests the age function"""
    # Avoid importing test module during normal operation
    import pytest

    # Happy path
    assert age(2000) == fmt_text(2000, 23)
    # Edge case
    assert age(current_year) == fmt_text(current_year, 0)
    # Negative cases
    with pytest.raises(ValueError):
        age(current_year + 1)
    with pytest.raises(ValueError):
        age("2000")
    with pytest.raises(ValueError):
        age(2000.1)


# Print example output
text = age(1983)
print(text)
