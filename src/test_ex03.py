# Exercise 3: Concat


def special_concat(item_1, item_2, item_3):
    """Concatenate three items using a special format."""
    if not all(isinstance(arg, str) for arg in (item_1, item_2, item_3)):
        raise TypeError("Arguments must be strings")

    return f"{item_1}, {item_2} & {item_3}"


# Print example output
print(special_concat("Cats", "Dogs", "Wolfs"))


def test_special_concat():
    """Test the special_concat function."""
    import pytest

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

    # Negative tests
    with pytest.raises(TypeError):
        special_concat(None, "Apple", "Cherry")
    with pytest.raises(TypeError):
        special_concat("Apple", None, "Cherry")
    with pytest.raises(TypeError):
        special_concat("Apple", "Banana", None)
