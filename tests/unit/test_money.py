# mypy: disable-error-code="operator"
"""Money tests"""

from decimal import Decimal

from money.currency import Currency
from money.exceptions import CurrencyMismatchError
from money.exceptions import InvalidAmountError
from money.exceptions import InvalidOperandError
from money.money import Money

import pytest


class TestMoney:
    """Money tests"""

    def test_construction(self):
        money = Money("3.95")
        assert money.amount == Decimal("3.95")
        assert money.currency == Currency.USD

        money = Money("1", Currency.USD)
        assert money.amount == Decimal("1")
        assert money.currency == Currency.USD

        money = Money("199", Currency.JPY)
        assert money.amount == Decimal("199")
        assert money.currency == Currency.JPY

        money = Money("192.325", Currency.KWD)
        assert money.amount == Decimal("192.325")
        assert money.currency == Currency.KWD

        with pytest.raises(
            InvalidAmountError,
            match=r"'3\.956' has too many decimal places for Currency\.USD",
        ):
            Money("3.956", Currency.USD)

        with pytest.raises(InvalidAmountError):
            # nonfractional currency
            Money("10.2", Currency.KRW)

    def test_from_sub_units(self):
        money = Money.from_sub_units(101, Currency.USD)
        assert money == Money("1.01", Currency.USD)

        money = Money.from_sub_units(5, Currency.JPY)
        assert money == Money("5", Currency.JPY)

    def test_sub_units(self):
        money = Money("1.01", Currency.USD)
        assert money.sub_units == 101

    def test_hash(self):
        assert hash(Money("1.2")) == hash(Money("1.2", Currency.USD))
        assert hash(Money("1.5")) != hash(Money("9.3"))
        assert hash(Money("99.3", Currency.CHF)) != hash(Money("99.3", Currency.USD))

    def test_tostring(self):
        assert str(Money("1.2")) == "USD 1.2"
        assert str(Money("3.6", Currency.CHF)) == "CHF 3.6"
        assert str(Money("88", Currency.JPY)) == "JPY 88"

    def test_less_than(self):
        assert Money("-1.2") < 0
        assert not Money("104.2") < 0
        assert not Money("0") < 0

        with pytest.raises(InvalidOperandError):
            Money("1.2") < 2  # noqa: B015

        assert Money("1.2") < Money("3.5")
        assert not Money("104.2") < Money("5.13")
        assert not Money("2.2") < Money("2.2")

        with pytest.raises(CurrencyMismatchError):
            Money("1.2", Currency.GBP) < Money("3.5", Currency.EUR)  # noqa: B015

        with pytest.raises(InvalidOperandError):
            Money("1.2") < 3.5  # noqa: B015

    def test_less_than_or_equal(self):
        assert Money("-1.2") <= 0
        assert not Money("104.2") < 0
        assert Money("0") <= 0

        with pytest.raises(InvalidOperandError):
            Money("2") <= 2  # noqa: B015

        assert Money("1.2") <= Money("3.5")
        assert not Money("104.2") <= Money("5.13")
        assert Money("2.2") <= Money("2.2")

        with pytest.raises(CurrencyMismatchError):
            Money("1.2", Currency.GBP) <= Money("3.5", Currency.EUR)  # noqa: B015

        with pytest.raises(InvalidOperandError):
            Money("1.2") <= 3.4  # noqa: B015

    def test_greater_than(self):
        assert Money("3.5") > 0
        assert not Money("-5.13") > 0
        assert not Money("0") > 0

        with pytest.raises(InvalidOperandError):
            Money("3.5") > 1  # noqa: B015

        assert Money("3.5") > Money("1.2")
        assert not Money("5.13") > Money("104.2")
        assert not Money("2.2") > Money("2.2")

        with pytest.raises(CurrencyMismatchError):
            Money("3.5", Currency.EUR) > Money("1.2", Currency.GBP)  # noqa: B015

        with pytest.raises(InvalidOperandError):
            Money("3.5") > 1.2  # noqa: B015

    def test_greater_than_or_equal(self):
        assert Money("3.5") >= 0
        assert not Money("-5.13") >= 0
        assert Money("0") >= 0

        with pytest.raises(InvalidOperandError):
            Money("3.5") >= 1  # noqa: B015

        assert Money("3.5") >= Money("1.2")
        assert not Money("5.13") >= Money("104.2")
        assert Money("2.2") >= Money("2.2")

        with pytest.raises(CurrencyMismatchError):
            Money("3.5", Currency.EUR) >= Money("1.2", Currency.GBP)  # noqa: B015

        with pytest.raises(InvalidOperandError):
            Money("3.5") >= 1.2  # noqa: B015

    def test_equal(self):
        assert Money("0") == 0
        assert Money("0", Currency.GBP) == 0
        assert not Money("6.9") == 0  # noqa: SIM201

        assert Money("3.5") == Money("3.5")
        assert Money("4.0", Currency.GBP) == Money("4.0", Currency.GBP)
        assert not Money("6.9") == Money("43")  # noqa: SIM201

        with pytest.raises(CurrencyMismatchError):
            Money("3.5", Currency.EUR) == Money("3.5", Currency.GBP)  # noqa: B015

        assert not Money("5.5") == 5.5  # noqa: SIM201
        assert not Money("6.5") == None  # noqa: SIM201,E711, do not replace with 'is True' as it tests '__eq__'
        assert not Money("7") == 7  # noqa: SIM201
        assert not Money("8.5") == Decimal("8.5")  # noqa: SIM201
        assert not Money("10") == True  # noqa: SIM201,E712, do not replace with 'is True' as it tests '__eq__'
        assert not Money("11") == "a-string"  # noqa: SIM201

        class AType:  # noqa: PLW1641
            def __eq__(self, other):
                return True

        assert Money("9") == AType()

    def test_not_equal(self):
        assert not Money("0") != 0  # noqa: SIM202

        assert Money("3.5") != Money("46.44")
        assert Money("4.0", Currency.GBP) != Money("12.01", Currency.GBP)
        assert not Money("6.9") != Money("6.9")  # noqa: SIM202

        with pytest.raises(CurrencyMismatchError):
            Money("3.5", Currency.EUR) != Money("23", Currency.GBP)  # noqa: B015

        assert Money("5.5") != 666.32
        assert Money("6.5") != None  # noqa: E711, do not replace with 'is None' as it tests '__eq__'
        assert Money("7") != 7
        assert Money("8.5") != Decimal("8.5")
        assert Money("10") != True  # noqa: E712, do not replace with 'is True' as it tests '__eq__'
        assert Money("11") != "a-string"

        class AType:
            def __neq__(self, other):
                return True

        assert Money("9") != AType()

    def test_bool(self):
        assert bool(Money("3.62")) is True
        assert bool(Money("0.00")) is False

    def test_add(self):
        assert Money("3.5") + Money("1.25") == Money("4.75")

        with pytest.raises(CurrencyMismatchError):
            Money("3.5", Currency.EUR) + Money("23", Currency.GBP)

        with pytest.raises(InvalidOperandError):
            Money("5.5") + 666.32

        with pytest.raises(InvalidOperandError):
            666.32 + Money("5.5")

    def test_subtract(self):
        assert Money("3.5") - Money("1.25") == Money("2.25")
        assert Money("4") - Money("5.5") == Money("-1.5")

        with pytest.raises(CurrencyMismatchError):
            Money("3.5", Currency.EUR) - Money("1.8", Currency.GBP)

        with pytest.raises(InvalidOperandError):
            Money("5.5") - 6.32

        with pytest.raises(InvalidOperandError):
            666.32 - Money("5.5")

    def test_multiply(self):
        assert Money("3.2") * 3 == Money("9.6")
        assert 3 * Money("3.2", Currency.EUR) == Money("9.6", Currency.EUR)
        assert Money("9.95") * Decimal("0.15") == Money("1.49")
        assert Money("3", Currency.JPY) * Decimal("0.2") == Money("1", Currency.JPY)
        assert Money("3", Currency.KRW) * Decimal("1.5") == Money("4", Currency.KRW)

        # since GNF has different subunits than JPY, the results are different even though
        # they have the same final decimal precision. hopefully this behavior is correct...
        assert Money("3", Currency.JPY) * Decimal("1.4995") == Money("4", Currency.JPY)
        assert Money("3", Currency.GNF) * Decimal("1.4995") == Money("4", Currency.GNF)

        with pytest.raises(InvalidOperandError):
            Money("3.2") * 3.2

        with pytest.raises(InvalidOperandError):
            3.2 * Money("3.2")

        with pytest.raises(InvalidOperandError):
            Money("5.5") * Money("1.2")

    def test_divide(self):
        assert Money("3.3") / 3 == Money("1.1")
        assert Money("9.95") / Decimal("0.24") == Money("41.46")
        assert Money("3", Currency.JPY) / Decimal("1.6") == Money("2", Currency.JPY)
        assert Money("3.6") / Money("2.5") == Decimal("1.44")

        with pytest.raises(InvalidOperandError):
            Money("5.5") / 3.2

        with pytest.raises(TypeError):
            Decimal("3") / Money("5.5")

        with pytest.raises(TypeError):
            3 / Money("5.5")

        with pytest.raises(ZeroDivisionError):
            Money("3") / Decimal("0")

        with pytest.raises(ZeroDivisionError):
            Money("3") / 0

        with pytest.raises(InvalidOperandError):
            Money("3") / 0.0

        with pytest.raises(ZeroDivisionError):
            Money("3.3") / Decimal("0.0")

        with pytest.raises(ZeroDivisionError):
            Money("3.3") / Money("0")

        with pytest.raises(CurrencyMismatchError):
            Money("3.5", Currency.EUR) / Money("1.8", Currency.GBP)

    def test_floor_divide(self):
        assert Money("3.3") // 3 == Money("1")
        assert Money("9.95") // Decimal("0.24") == Money("41")
        assert Money("3", Currency.JPY) // Decimal("1.6") == Money("1", Currency.JPY)
        assert Money("3.6") // Money("2.5") == Decimal("1")

        with pytest.raises(InvalidOperandError):
            Money("5.5") // 3.2

        with pytest.raises(TypeError):
            3 // Money("5.5")

        with pytest.raises(ZeroDivisionError):
            Money("3") // 0

        with pytest.raises(ZeroDivisionError):
            Money("3.3") // Decimal("0.0")

        with pytest.raises(InvalidOperandError):
            Money("3.3") // 0.0

        with pytest.raises(ZeroDivisionError):
            Money("3.3") // Money("0")

        with pytest.raises(ZeroDivisionError):
            Money("3.3") // 0

        with pytest.raises(CurrencyMismatchError):
            Money("3.5", Currency.EUR) // Money("1.8", Currency.GBP)

    def test_mod(self):
        assert Money("3.3") % 3 == Money("0.3")
        assert Money("3", Currency.JPY) % Decimal("2") == Money("1", Currency.JPY)
        assert Money("3") % Money("2") == Decimal("1")

        with pytest.raises(InvalidOperandError):
            Money("5.5") % 3.2

        with pytest.raises(TypeError):
            3 % Money("5.5")

        with pytest.raises(ZeroDivisionError):
            Money("3.3") % 0

        with pytest.raises(ZeroDivisionError):
            Money("3.3") % Decimal("0.0")

        with pytest.raises(InvalidOperandError):
            Money("3.3") % 0.0

        with pytest.raises(CurrencyMismatchError):
            Money("3.5", Currency.EUR) % Money("1.8", Currency.GBP)

    def test_neg(self):
        assert -Money("5.23") == Money("-5.23")
        assert -Money("-1.35") == Money("1.35")

    def test_pos(self):
        assert +Money("5.23") == Money("5.23")
        assert +Money("-1.35") == Money("-1.35")

    def test_abs(self):
        assert abs(Money("5.23")) == Money("5.23")
        assert abs(Money("-1.35")) == Money("1.35")

    def test_format(self):
        assert Money("3.24").format() == "$3.24"
        assert Money("5.56", Currency.EUR).format("en_UK") == "€5.56"
        assert Money("10", Currency.JPY).format() == "¥10"
        assert Money("94", Currency.JPY).format("ja_JP") == "￥94"

    def test_assert_same_currency(self):
        with pytest.raises(
            CurrencyMismatchError,
            match=r"'self' currency is Currency\.GBP but 'other' currency is Currency\.EUR",
        ):
            Money("1.2", Currency.GBP) < Money("3.5", Currency.EUR)  # noqa: B015
