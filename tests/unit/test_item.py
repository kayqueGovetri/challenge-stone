import pytest

from src import Item


def test_quantity_negative():
    with pytest.raises(ValueError):
        Item(quantity=-1, name="banana", price_per_unit=0)


def test_price_per_unit_negative():
    with pytest.raises(ValueError):
        Item(quantity=0, name="banana", price_per_unit=-10)
