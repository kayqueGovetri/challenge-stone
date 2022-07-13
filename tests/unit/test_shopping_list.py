import pytest
from faker import Faker

from src import Item, ShoppingList

fake = Faker()


items = [
    Item(name="banana", quantity=1, price_per_unit=100),
]
emails = [fake.email() for _ in range(0, 3)]


@pytest.mark.parametrize(
    "items,emails,expected",
    [
        (
            [Item(name="banana", quantity=1, price_per_unit=100)],
            [
                "huertalisa@example.com",
                "leahrodriguez@example.net",
                "joseph36@example.net",
            ],
            {
                "huertalisa@example.com": 33,
                "leahrodriguez@example.net": 33,
                "joseph36@example.net": 34,
            },
        ),
        (
            [Item(name="banana", quantity=1, price_per_unit=102)],
            [
                "huertalisa@example.com",
                "leahrodriguez@example.net",
                "joseph36@example.net",
                "joseph38@example.com",
            ],
            {
                "huertalisa@example.com": 25,
                "leahrodriguez@example.net": 25,
                "joseph36@example.net": 25,
                "joseph38@example.com": 27,
            },
        ),
        (
            [Item(name="banana", quantity=1, price_per_unit=1)],
            [
                "melanie12@example.net",
                "melissa21@example.com",
                "rebeccagood@example.org",
            ],
            {
                "melanie12@example.net": 0,
                "melissa21@example.com": 0,
                "rebeccagood@example.org": 1,
            },
        ),
    ],
)
def test_validate_bill_to_pay(items, emails, expected):
    shopping_list = ShoppingList(items=items, emails=emails)
    assert shopping_list.bill_to_pay() == expected
