"""Custom exceptions for money operations"""


class InvalidAmountError(ValueError):
    pass


class CurrencyMismatchError(ValueError):
    pass


class InvalidOperandError(ValueError):
    pass
