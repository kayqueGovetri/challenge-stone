def validate_is_empty_list(list_to_validate: list, name: str) -> bool:
    if not list_to_validate:
        raise ValueError(f"{name} items is empty")

    return True


def validate_duplicate_items_in_list(list_to_validate: list, name: str) -> bool:
    set_to_validate = set(list_to_validate)

    if len(set_to_validate) != len(list_to_validate):
        raise ValueError(f"{name} contains items duplicates")

    return True


def validate_is_instance_list(list_to_validate: list, name: str) -> bool:
    if not isinstance(list_to_validate, list):
        raise ValueError(f"{name} not a list")

    return True
