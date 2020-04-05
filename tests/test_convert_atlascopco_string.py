import pytest

from various_methods import VariousMethods

variousMethods = VariousMethods()

@pytest.mark.parametrize(
    "input,expected",
    [
        (87, "ERROR:)"),
        (15, "AtlasCopco"),
        (9, "Atlas"),
        (20, "Copco"),
        (7, "7")
    ])
def test_convert_to_atlas_string(input, expected):
    actual = variousMethods.ConvertToAtlasCopcoString(input)
    assert actual == expected

@pytest.mark.parametrize(
    "input,expected",
    [
        (0, pytest.raises(ValueError)),
        (101, pytest.raises(ValueError))
    ],
)
def test_convert_to_atlas_string_raises_value_error(input, expected):
    with expected:
        variousMethods.ConvertToAtlasCopcoString(input)