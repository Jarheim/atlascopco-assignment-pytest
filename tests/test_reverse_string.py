import pytest

from various_methods import VariousMethods

variousMethods = VariousMethods()

@pytest.mark.parametrize(
    "input,expected",
    [
        ("abc123$\"", "\"$321cba"),
        ("a", "a")
    ])
def test_reverse_string(input, expected):
    actual = variousMethods.ReverseString(input)
    assert actual == expected

@pytest.mark.parametrize(
    "input,expected",
    [
        (None, pytest.raises(ValueError)),
        ("", pytest.raises(ValueError))
    ],
)
def test_reverse_string_raises_value_error(input, expected):
    with expected:
        variousMethods.ReverseString(input)
