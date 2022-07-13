from typing import List

from src import Item, utils


class ShoppingList:
    def __init__(self, items: List[Item], emails: List[str]):
        self.__items = items
        self.__emails = emails
        self.validate_emails()
        self.validate_items()

    def bill_to_pay(self) -> dict:
        total_amount_to_emails = int(self.amount / len(self.emails))
        return self.get_dict_to_values_to_emails(total_amount_to_emails)

    def get_dict_to_values_to_emails(self, total_amount_to_emails: int) -> dict:
        mutable_total = self.amount
        len_emails = len(self.emails) - 1
        response = {}
        for index, email in enumerate(self.emails):
            if index == len_emails:
                response.update({email: mutable_total})
            else:
                response.update({email: total_amount_to_emails})
            mutable_total -= int(total_amount_to_emails)
        return response

    @property
    def amount(self):
        return sum(self.__items)

    @property
    def items(self):
        return self.__items

    @property
    def emails(self):
        return self.__emails

    def validate_emails(self):
        utils.validate_is_instance_list(self.emails, "Emails")
        utils.validate_is_empty_list(self.emails, "Emails")
        utils.validate_duplicate_items_in_list(self.emails, "Emails")

    def validate_items(self):
        utils.validate_is_instance_list(self.items, "Items")
        utils.validate_is_empty_list(self.items, "Items")
        utils.validate_duplicate_items_in_list(self.items, "Items")
