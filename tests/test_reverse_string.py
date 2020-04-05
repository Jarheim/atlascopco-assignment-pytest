import pytest

from various_methods import VariousMethods

variousMethods = VariousMethods()

def test_reverse_string():
    actual = variousMethods.ReverseString("abc123$\"")
    assert actual == "\"$321cba"
    print(actual)

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
