"""Money rounding tests"""

from decimal import ROUND_HALF_UP
from decimal import Decimal

from money import Currency
from money.currency import CurrencyHelper
from money.money import Money


class MoneyRoundingHalfUp(Money):
    """Money class with default rounding mode: half even"""

    rounding_mode = ROUND_HALF_UP


class TestMoneyRounding:
    """Money rounding tests"""

    def test_divide_with_decimal(self):
        money_half_even_division = Money("8.67") / Decimal("1.20")
        assert money_half_even_division == Money("7.22")
        assert money_half_even_division.amount == Decimal("7.22")

        money_division = MoneyRoundingHalfUp("8.67") / Decimal("1.20")
        assert money_division == MoneyRoundingHalfUp("7.23")
        assert money_division.amount == Decimal("7.23")

    def test_multiply_with_decimal(self):
        money_half_even_multiplication = Money("3") * Decimal("2.115")
        assert money_half_even_multiplication == Money("6.34")
        assert money_half_even_multiplication.amount == Decimal("6.34")

        money_multiplication = MoneyRoundingHalfUp("3") * Decimal("2.115")
        assert money_multiplication == MoneyRoundingHalfUp("6.35")
        assert money_multiplication.amount == Decimal("6.35")


def test_round_amount():
    assert CurrencyHelper.round_amount(Currency.USD, Decimal("12.235")) == Decimal("12.24")
    assert CurrencyHelper.round_amount(Currency.USD, Decimal("12.245")) == Decimal("12.24")
    assert CurrencyHelper.round_amount(Currency.USD, Decimal("12.246")) == Decimal("12.25")
    assert CurrencyHelper.round_amount(Currency.USD, Decimal("12.245"), rounding_mode=ROUND_HALF_UP) == Decimal("12.25")
    assert CurrencyHelper.round_amount(Currency.JPY, Decimal("12.5"), rounding_mode=ROUND_HALF_UP) == Decimal("13")
