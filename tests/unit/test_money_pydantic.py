import json

from decimal import Decimal

from money.currency import Currency
from money.money import Money

import pytest

from pydantic import TypeAdapter
from pydantic import ValidationError


class TestPydantic:
    """Money serialization tests"""

    def test_money_dump_python(self):
        # given
        money = Money("199", Currency.JPY)
        expected = {"amount": Decimal("199"), "currency": Currency.JPY}
        # when
        actual = TypeAdapter(Money).dump_python(money)
        # then
        assert actual == expected

    def test_money_dump_json(self):
        # given
        money = Money("199", Currency.JPY)
        expected = {"amount": "199", "currency": "JPY"}
        # when
        actual = TypeAdapter(Money).dump_json(money)
        # then
        assert json.loads(actual) == expected

    def test_money_load_python_typed(self):
        # given
        payload = {"amount": Decimal("199"), "currency": Currency.JPY}
        # when
        actual = TypeAdapter(Money).validate_python(payload)
        # then
        assert actual == Money("199", Currency.JPY)

    def test_money_load_python_cast(self):
        # given
        expected = Money("199", Currency.JPY)
        payload = {"amount": "199", "currency": "JPY"}
        # when
        actual = TypeAdapter(Money).validate_python(payload)
        # then
        assert actual == expected

    def test_money_invalidates_amount(self):
        # given
        payload = {"amount": "hello", "currency": "JPY"}
        # when
        with pytest.raises(ValidationError):
            TypeAdapter(Money).validate_python(payload)

    def test_money_invalidates_currency(self):
        # given
        payload = {"amount": "199", "currency": "XXX"}
        # when
        with pytest.raises(ValidationError):
            TypeAdapter(Money).validate_python(payload)

    def test_money_invalidates_rounded_by_currency(self):
        # given
        payload = {"amount": "3.10", "currency": "KRW"}
        # when
        with pytest.raises(ValidationError):
            TypeAdapter(Money).validate_python(payload)

    def test_money_generates_schema(self):
        actual = TypeAdapter(Money).json_schema()
        assert actual["type"] == "object"
        assert actual["required"] == ["amount", "currency"]
