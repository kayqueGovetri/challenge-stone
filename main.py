from src import Item, ShoppingList
from faker import Faker

fake = Faker()

if __name__ == "__main__":
    items = [
        Item(name="banana", quantity=1, price_per_unit=100),
    ]
    emails = [fake.email() for _ in range(0, 3)]
    shopping_list = ShoppingList(items=items, emails=emails)
    response = shopping_list.bill_to_pay()
    print(response)
