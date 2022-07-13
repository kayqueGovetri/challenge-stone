import pytest
from faker import Faker

from src import utils

fake = Faker()

emails = [fake.email() for _ in range(0, 3)]


@pytest.mark.parametrize(
    "lists",
    [
        [fake.email() for _ in range(0, 3)],
        [fake.pyint() for _ in range(0, 3)],
        [fake.name() for _ in range(0, 3)],
    ],
)
def test_validate_is_instance_list_success(lists):
    assert utils.validate_is_instance_list(list_to_validate=lists, name="test")


@pytest.mark.parametrize(
    "lists",
    [
        [fake.email() for _ in range(0, 3)],
        [fake.pyint() for _ in range(0, 3)],
        [fake.name() for _ in range(0, 3)],
    ],
)
def test_validate_duplicate_items_in_list_success(lists):
    assert utils.validate_duplicate_items_in_list(list_to_validate=lists, name="test")


@pytest.mark.parametrize(
    "lists",
    [
        [fake.email() for _ in range(0, 3)],
        [fake.pyint() for _ in range(0, 3)],
        [fake.name() for _ in range(0, 3)],
    ],
)
def test_validate_is_empty_list_success(lists):
    assert utils.validate_is_empty_list(list_to_validate=lists, name="test")


@pytest.mark.parametrize(
    "lists",
    [
        {fake.email(): index for index in range(0, 3)},
        (fake.pyint() for _ in range(0, 3)),
        fake.name(),
        fake.pyint(),
        fake.pybool(),
    ],
)
def test_validate_is_instance_list_error(lists):
    with pytest.raises(ValueError):
        utils.validate_is_instance_list(list_to_validate=lists, name="test")


@pytest.mark.parametrize(
    "lists",
    [
        [1, 1, 2],
        ["a", "a"],
    ],
)
def test_validate_duplicate_items_in_list_error(lists):
    with pytest.raises(ValueError):
        utils.validate_duplicate_items_in_list(list_to_validate=lists, name="test")


@pytest.mark.parametrize(
    "lists",
    [
        [],
    ],
)
def test_validate_is_empty_list_error(lists):
    with pytest.raises(ValueError):
        utils.validate_is_empty_list(list_to_validate=lists, name="test")
