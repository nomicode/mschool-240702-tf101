# Exercise 3: Concat

# pylint: disable=missing-docstring


def special_concat(item_1, item_2, item_3):
    """Concatenate three items using a special format.

    Specifically:
    - Items separated by commas
    - An ampersand before the last item
    - No Oxford comma

    Args:
        item_1 (str): First item
        item_2 (str): Second item
        item_3 (str): Third item
    Raises:
        ValueError: If any argument is not a string
    Returns:
        str: Concatenated string
    """
    if not all(isinstance(arg, str) for arg in (item_1, item_2, item_3)):
        raise ValueError("All arguments must be strings")

    return f"{item_1}, {item_2} & {item_3}"


def test_special_concat():
    """Tests the special_concat function."""
    # Avoid importing test module during normal operation
    # pylint: disable=import-outside-toplevel
    import pytest

    # trunk-ignore-all(bandit/B101)
    # Happy path
    assert (
        special_concat("Apple", "Banana", "Cherry") == "Apple, Banana & Cherry"
    )
    # Edge cases
    # "Unix was not designed to stop you from doing stupid things, because
    # that would also stop you from doing clever things." - Doug Gwyn
    assert special_concat("", "Banana", "Cherry") == ", Banana & Cherry"
    assert special_concat("Apple", "", "Cherry") == "Apple,  & Cherry"
    assert special_concat("Apple", "Banana", "") == "Apple, Banana & "
    # Just for laughs
    assert special_concat("&", "&", "&") == "&, & & &"
    # Negative case
    with pytest.raises(ValueError):
        # Non-string input
        special_concat(123, "Banana", "Cherry")


# Print example output
print(special_concat("Cats", "Dogs", "Wolfs"))
