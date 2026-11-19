"""Class representing a monetary amount"""

from dataclasses import dataclass
from decimal import ROUND_HALF_EVEN
from decimal import Decimal
from typing import ClassVar
from typing import Literal
from typing import Self
from typing import Union
from typing import overload

from money.currency import Currency
from money.currency import CurrencyHelper
from money.exceptions import CurrencyMismatchError
from money.exceptions import InvalidAmountError
from money.exceptions import InvalidOperandError

from babel.numbers import format_currency


@dataclass(frozen=True)
class Money:
    """Class representing a monetary amount"""

    amount: Decimal
    currency: Currency

    rounding_mode: ClassVar[str] = ROUND_HALF_EVEN

    def __init__(self, amount: str | Decimal, currency: Currency = Currency.USD) -> None:
        self.__dict__["amount"] = Decimal(amount)
        self.__dict__["currency"] = currency
        self.__post_init__()

    def __post_init__(self):
        if self._round(self.amount, self.currency) != Decimal(self.amount):
            raise InvalidAmountError(f"'{self.amount}' has too many decimal places for {self.currency}")

    @classmethod
    def from_sub_units(cls, sub_units: int, currency: Currency = Currency.USD) -> Self:
        """Creates a Money instance from sub-units."""
        sub_units_per_unit = CurrencyHelper.sub_unit_for_currency(currency)
        return cls(Decimal(sub_units) / Decimal(sub_units_per_unit), currency)

    @property
    def sub_units(self) -> int:
        """Converts the amount to sub-units"""
        sub_units_per_unit = CurrencyHelper.sub_unit_for_currency(self.currency)
        return int(self.amount * sub_units_per_unit)

    def __hash__(self) -> int:
        return hash((self.amount, self.currency))

    def __repr__(self) -> str:
        return "{} {}".format(self.currency.name, self.amount)  # noqa: UP032

    def __lt__(self, other: Union["Money", Literal[0]]) -> bool:
        if isinstance(other, int) and other == 0:
            return self.amount < 0

        if not isinstance(other, Money):
            raise InvalidOperandError

        self._assert_same_currency(other)
        return self.amount < other.amount

    def __le__(self, other: Union["Money", Literal[0]]) -> bool:
        if isinstance(other, int) and other == 0:
            return self.amount <= 0

        if not isinstance(other, Money):
            raise InvalidOperandError

        self._assert_same_currency(other)
        return self.amount <= other.amount

    def __gt__(self, other: Union["Money", Literal[0]]) -> bool:
        if isinstance(other, int) and other == 0:
            return self.amount > 0

        if not isinstance(other, Money):
            raise InvalidOperandError

        self._assert_same_currency(other)
        return self.amount > other.amount

    def __ge__(self, other: Union["Money", Literal[0]]) -> bool:
        if isinstance(other, int) and other == 0:
            return self.amount >= 0

        if not isinstance(other, Money):
            raise InvalidOperandError

        self._assert_same_currency(other)
        return self.amount >= other.amount

    def __eq__(self, other: object) -> bool:
        if isinstance(other, int) and other == 0:
            return self.amount == 0

        if not isinstance(other, Money):
            return NotImplemented

        self._assert_same_currency(other)
        return self.amount == other.amount

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __bool__(self):
        return bool(self.amount)

    def __add__(self, other: "Money") -> "Money":
        if not isinstance(other, Money):
            raise InvalidOperandError

        self._assert_same_currency(other)
        return self.__class__(str(self.amount + other.amount), self.currency)

    def __radd__(self, other: "Money") -> "Money":
        return self.__add__(other)

    def __sub__(self, other: "Money") -> "Money":
        if not isinstance(other, Money):
            raise InvalidOperandError

        self._assert_same_currency(other)
        return self.__class__(str(self.amount - other.amount), self.currency)

    def __rsub__(self, other: "Money") -> "Money":
        return self.__sub__(other)

    def __mul__(self, other: Decimal | int) -> "Money":
        if not isinstance(other, (Decimal, int)):
            raise InvalidOperandError

        amount = self._round(self.amount * other, self.currency)
        return self.__class__(str(amount), self.currency)

    def __rmul__(self, other: Decimal | int) -> "Money":
        return self.__mul__(other)

    def __div__(self, other: Decimal | int) -> "Money":
        return self.__truediv__(other)

    @overload
    def __truediv__(self, other: "Money") -> Decimal: ...

    @overload
    def __truediv__(self, other: Decimal | int) -> "Money": ...

    def __truediv__(self, other: Union["Money", Decimal, int]) -> Union["Money", Decimal]:
        if isinstance(other, Money):
            self._assert_same_currency(other)
            if other.amount == Decimal("0"):
                raise ZeroDivisionError
            return Decimal(self.amount / other.amount)

        elif isinstance(other, (Decimal, int)):
            if other == 0:
                raise ZeroDivisionError
            amount = self._round(self.amount / Decimal(other), self.currency)
            return self.__class__(str(amount), self.currency)

        raise InvalidOperandError

    @overload
    def __floordiv__(self, other: "Money") -> Decimal: ...

    @overload
    def __floordiv__(self, other: Decimal | int) -> "Money": ...

    def __floordiv__(self, other: Union["Money", Decimal, int]) -> Union["Money", Decimal]:
        if isinstance(other, Money):
            self._assert_same_currency(other)
            if other.amount == Decimal("0"):
                raise ZeroDivisionError
            return Decimal(self.amount // other.amount)

        elif isinstance(other, (Decimal, int)):
            if other == 0:
                raise ZeroDivisionError
            amount = self._round(self.amount // Decimal(other), self.currency)
            return self.__class__(str(amount), self.currency)

        raise InvalidOperandError

    def __mod__(self, other: Union["Money", Decimal, int]) -> Union["Money", Decimal]:
        if isinstance(other, Money):
            self._assert_same_currency(other)
            if other.amount == Decimal("0"):
                raise ZeroDivisionError
            return Decimal(self.amount % other.amount)

        elif isinstance(other, (Decimal, int)):
            if other == 0:
                raise ZeroDivisionError
            amount = self._round(self.amount % other, self.currency)
            return self.__class__(str(amount), self.currency)

        raise InvalidOperandError

    def __neg__(self) -> "Money":
        return self.__class__(str(-self.amount), self.currency)

    def __pos__(self) -> "Money":
        return self.__class__(str(+self.amount), self.currency)

    def __abs__(self) -> "Money":
        return self.__class__(str(abs(self.amount)), self.currency)

    def format(self, locale: str = "en_US") -> str:
        """Returns a string of the currency formatted for the specified locale"""

        return format_currency(self.amount, self.currency.name, locale=locale)

    def _assert_same_currency(self, other: "Money") -> None:
        if self.currency != other.currency:
            raise CurrencyMismatchError(f"'self' currency is {self.currency} but 'other' currency is {other.currency}")

    @classmethod
    def _round(cls, amount: Decimal, currency: Currency) -> Decimal:
        return CurrencyHelper.round_amount(currency, amount, cls.rounding_mode)
