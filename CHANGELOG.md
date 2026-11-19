# CHANGELOG

## 4.0.0

### Breaking changes

- **Requires Python >= 3.11**.

## 3.1.0

### Breaking changes

- **Default rounding changed to banker's rounding** (`ROUND_HALF_EVEN`, was
  `ROUND_HALF_UP`). Results of multiplication and division that land on a
  half-unit may differ. For example, a value rounding to `0.125` at 2 decimals
  now yields `0.12` instead of `0.13`.
- **Division and modulo between two `Money` return `Decimal`** instead of
  `float`. `Money / Money`, `Money // Money` and `Money % Money` now return a
  `Decimal` ratio.
- **Multiplication and division by `float` is no longer allowed**. Operands must
  be `int` or `Decimal`; passing a `float` now raises `InvalidOperandError`.
  Use a `Decimal` instead (e.g. `m * Decimal("1.5")`).
- **Equality with non-`Money` no longer raises**. `money == something_else`
  (and `!=`) now returns `False`/`True` instead of raising `InvalidOperandError`,
  so `Money` behaves correctly in mixed collections and `in` checks.
- **Richer exception messages**. `InvalidAmountError` and `CurrencyMismatchError`
  now include the offending values in their message (e.g. which amount/currency
  caused the failure). The custom exceptions are now plain `ValueError`
  subclasses with no forced message, so they can be raised with a custom message.
- **Requires Python >= 3.9**.

### Packaging

- **Renamed package**: install with `pip install money-iso` (was `py-money`).
  The import path is unchanged: `from money import Money, Currency`.
- **Top-level imports added**: `Money` and `Currency` are now exported directly
  from the `money` package (`from money import Money, Currency`), instead of
  requiring `from money.money import Money` / `from money.currency import Currency`.
- **Ships type information** (`py.typed`): the library is now fully typed and
  type checkers (mypy, pyright) will pick up its annotations.
- New runtime dependencies: `pydantic` (>=2.7) and `typing-extensions`.

### New features

- **Pydantic v2 support**: `Money` can now be validated and serialized through
  pydantic (e.g. `TypeAdapter(Money)`). It serializes to
  `{"amount": ..., "currency": ...}` and can be built back from that payload,
  including from plain strings (`{"amount": "199", "currency": "JPY"}`).
- **Configurable rounding mode**: a new public helper
  `CurrencyHelper.round_amount(currency, amount, rounding_mode=...)` exposes
  rounding with any Python rounding mode. `Money` rounds through a
  `rounding_mode` class attribute that can be overridden on a subclass.
- **Comparisons against `0`**: `Money` instances can now be compared directly to
  the literal `0` regardless of currency, e.g. `m > 0`, `m == 0`, `m <= 0`.
  This is handy for sign checks without constructing a zero-amount `Money`.
- **`Decimal` amounts accepted**: the `Money(...)` constructor now accepts a
  `Decimal` in addition to a `str` for the amount.

## 0.5.0

### Fix BYR subunits and add new BYN currency Latest

- Adds new BYN Belarusian currency
- Fixes Belarusian display name misspelling
- Bumps version to 0.5.0
- Updates author info

## 0.4.0

### Allow more versions of babel

- Allows this package to work with versions of babel >= 2.4.0 and < 3.0

## 0.3.0

### Add ability to work with subunits

- Adds from_sub_units method to create money from subunits
- Adds sub_units property to retrieve the monetary amount in subunits

## 0.2.0

Add support for dividing money by money

## 0.1.1

Improve installation

## 0.1.0

Initial release
