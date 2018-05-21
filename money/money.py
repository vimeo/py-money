"""Class representing a monetary amount"""

from typing import Union
from decimal import Decimal
from decimal import ROUND_CEILING
from decimal import ROUND_DOWN
from decimal import ROUND_FLOOR
from decimal import ROUND_HALF_DOWN
from decimal import ROUND_HALF_EVEN
from decimal import ROUND_HALF_UP
from decimal import ROUND_UP
from decimal import ROUND_05UP
from babel.numbers import format_currency
from money.currency import Currency
from money.currency import CurrencyHelper
from money.exceptions import InvalidAmountError, CurrencyMismatchError, InvalidOperandError

# pylint: disable=invalid-name
DecimalRoundingType = Union[
    ROUND_CEILING,
    ROUND_DOWN,
    ROUND_FLOOR,
    ROUND_HALF_DOWN,
    ROUND_HALF_EVEN,
    ROUND_HALF_UP,
    ROUND_UP,
    ROUND_05UP,
]

class Money:
    """Class representing a monetary amount"""

    rounding_per_operation = True
    rounding_type = ROUND_HALF_UP

    def __init__(self, amount: str, currency: Currency = Currency.USD) -> None:
        self._amount = Decimal(amount)
        self._currency = currency

        if self._round(self._amount, currency) != Decimal(amount):
            raise InvalidAmountError

    @property
    def amount(self) -> Decimal:
        """Returns the numeric amount"""

        return self._amount

    @property
    def currency(self) -> Currency:
        """Returns the currency"""

        return self._currency

    def __hash__(self) -> str:
        return hash((self._amount, self._currency))

    def __repr__(self) -> str:
        return "{} {}".format(self._currency.name, self._amount)

    def __lt__(self, other: 'Money') -> bool:
        if not isinstance(other, Money):
            raise InvalidOperandError

        self._assert_same_currency(other)
        return self.amount < other.amount

    def __le__(self, other: 'Money') -> bool:
        if not isinstance(other, Money):
            raise InvalidOperandError

        self._assert_same_currency(other)
        return self.amount <= other.amount

    def __gt__(self, other: 'Money') -> bool:
        if not isinstance(other, Money):
            raise InvalidOperandError

        self._assert_same_currency(other)
        return self.amount > other.amount

    def __ge__(self, other: 'Money') -> bool:
        if not isinstance(other, Money):
            raise InvalidOperandError

        self._assert_same_currency(other)
        return self.amount >= other.amount

    def __eq__(self, other: 'Money') -> bool:
        if not isinstance(other, Money):
            raise InvalidOperandError

        self._assert_same_currency(other)
        return self.amount == other.amount

    def __ne__(self, other: 'Money') -> bool:
        return not self == other

    def __bool__(self):
        return bool(self._amount)

    def __add__(self, other: 'Money') -> 'Money':
        if not isinstance(other, Money):
            raise InvalidOperandError

        self._assert_same_currency(other)
        return self.__class__(str(self.amount + other.amount), self.currency)

    def __radd__(self, other: 'Money') -> 'Money':
        return self.__add__(other)

    def __sub__(self, other: 'Money') -> 'Money':
        if not isinstance(other, Money):
            raise InvalidOperandError

        self._assert_same_currency(other)
        return self.__class__(str(self.amount - other.amount), self.currency)

    def __rsub__(self, other: 'Money') -> 'Money':
        return self.__sub__(other)

    def __mul__(self, other: float) -> 'Money':
        if isinstance(other, Money):
            raise InvalidOperandError

        amount = self._round(self._amount * Decimal(other), self._currency)
        return self.__class__(str(amount), self._currency)

    def __rmul__(self, other: float) -> 'Money':
        return self.__mul__(other)

    def __div__(self, other: float) -> 'Money':
        return self.__truediv__(other)

    def __truediv__(self, other: Union['Money', float]) -> Union['Money', float]:
        if isinstance(other, Money):
            self._assert_same_currency(other)
            if other.amount == Decimal('0'):
                raise ZeroDivisionError
            return float(self.amount / other.amount)

        else:
            if other == 0:
                raise ZeroDivisionError
            amount = self._round(self._amount / Decimal(other), self._currency)
            return self.__class__(str(amount), self._currency)

    def __floordiv__(self, other: Union['Money', float]) -> Union['Money', float]:
        if isinstance(other, Money):
            self._assert_same_currency(other)
            if other.amount == Decimal('0'):
                raise ZeroDivisionError
            return float(self.amount // other.amount)

        else:
            if other == 0:
                raise ZeroDivisionError
            amount = self._round(self._amount // Decimal(other), self._currency)
            return self.__class__(str(amount), self._currency)

    def __mod__(self, other: Union['Money', float]) -> Union['Money', float]:
        if isinstance(other, Money):
            self._assert_same_currency(other)
            if other.amount == Decimal('0'):
                raise ZeroDivisionError
            return float(self.amount % other.amount)

        else:
            if other == 0:
                raise ZeroDivisionError
            amount = self._round(self._amount % Decimal(other), self._currency)
            return self.__class__(str(amount), self._currency)

    def __neg__(self) -> 'Money':
        return self.__class__(str(-self._amount), self._currency)

    def __pos__(self) -> 'Money':
        return self.__class__(str(+self._amount), self._currency)

    def __abs__(self) -> 'Money':
        return self.__class__(str(abs(self._amount)), self._currency)

    def format(self, locale: str = 'en_US') -> str:
        """Returns a string of the currency formatted for the specified locale"""

        return format_currency(self.amount, self.currency.name, locale=locale)

    def _assert_same_currency(self, other: 'Money') -> None:
        if self.currency != other.currency:
            raise CurrencyMismatchError

    @staticmethod
    def _round(amount: Decimal, currency: Currency) -> Decimal:
        rounding_per_operation = Money.rounding_per_operation

        if not rounding_per_operation:
            return amount

        rounding_type = Money.rounding_type

        sub_units = CurrencyHelper.sub_unit_for_currency(currency)
        # rstrip is necessary because quantize treats 1. differently from 1.0
        rounded_to_subunits = amount.quantize(Decimal(str(1 / sub_units).rstrip('0')),\
                                              rounding=rounding_type)
        decimal_precision = CurrencyHelper.decimal_precision_for_currency(currency)
        return rounded_to_subunits.quantize(\
                   Decimal(str(1 / (10 ** decimal_precision)).rstrip('0')),\
                   rounding=rounding_type)

    @classmethod
    def set_rounding_per_operation(cls, value: bool) -> None:
        """Set the whether to apply rounding after certain operations class-wide"""

        if value is not True and value is not False:
            raise TypeError

        Money.rounding_per_operation = value

    @classmethod
    def set_rounding_type(cls, value: DecimalRoundingType) -> None:
        """If ``rounding_per_operation`` is set, this determines the rounding method to use"""

        if value not in [ROUND_CEILING, ROUND_DOWN, ROUND_FLOOR,
                         ROUND_HALF_DOWN, ROUND_HALF_EVEN, ROUND_HALF_UP,
                         ROUND_UP, ROUND_05UP,]:
            raise TypeError

        Money.rounding_type = value
