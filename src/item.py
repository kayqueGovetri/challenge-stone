class Item:
    def __init__(self, name: str, quantity: int, price_per_unit: int):
        self.name = name
        self.quantity = quantity
        self.price_per_unit = price_per_unit
        self.__amount = self.get_amount()

    @property
    def name(self) -> str:
        return self.__name

    @property
    def amount(self) -> int:
        return self.__amount

    @property
    def quantity(self) -> int:
        return self.__quantity

    @property
    def price_per_unit(self) -> int:
        return self.__price_per_unit

    @name.setter
    def name(self, new_name: str):
        self.__name = new_name

    @quantity.setter
    def quantity(self, new_amount: int):
        if new_amount < 0:
            raise ValueError("Quantity cannot be negative.")
        self.__quantity = new_amount

    @price_per_unit.setter
    def price_per_unit(self, new_price_per_unit: int):
        if new_price_per_unit < 0:
            raise ValueError("Price per unit cannot be negative.")
        self.__price_per_unit = new_price_per_unit

    def get_amount(self):
        return self.price_per_unit * self.quantity

    def __add__(self, other):
        if isinstance(other, int):
            return self.amount + other
        return self.amount + other.amount

    def __radd__(self, other):
        return self.__add__(other)

    def __eq__(self, other):
        if isinstance(other, Item):
            return self.name == other.name

        return False

    def __hash__(self):
        return hash(self.name)
