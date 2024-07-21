# Exercise 3: Concat


def special_concat(item_1, item_2, item_3):
    """Concatenate three items using a special format."""
    if not all(isinstance(arg, str) for arg in (item_1, item_2, item_3)):
        raise ValueError("All arguments must be strings")

    return f"{item_1}, {item_2} & {item_3}"


def test_special_concat():
    """Test the special_concat function."""
    # Module only used for testing
    import pytest

<<<<<<< HEAD:src/test_ex03.py
    # trunk-ignore-all(bandit/B101)
=======
>>>>>>> 32b77da (Add solution and tests for exercise 3):course/ms/csec/tf/101/1/src/test_ex03.py
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
    with pytest.raises(ValueError):
        # Non-string inputs
        special_concat("Apple", None, "Cherry")
        special_concat("Apple", "Banana", None)


# Print example output
print(special_concat("Cats", "Dogs", "Wolfs"))
