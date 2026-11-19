# money-iso

[![Latest PyPI version](https://badge.fury.io/py/money-iso.svg)](https://badge.fury.io/py/money-iso)

Money class for Python 3. Unlike other Python money classes, this class enforces that all monetary amounts are represented with the correct number of decimal places for the currency. For example, 3.678 USD is invalid, as is 5.5 JPY.

Drop-in replacement for [py-money](https://github.com/vimeo/py-money).

## Installation

Install the latest release with:

```
pip install money-iso
```

## Usage

A Money object can be created with an amount (specified as a string) and a currency from the Currency class.

```python
>>> from money.money import Money
>>> from money.currency import Currency
>>> m = Money('9.95', Currency.GBP)
>>> m
GBP 9.95
```

Money objects can also be created from and converted to sub units.

```python
>>> m = Money.from_sub_units(499, Currency.USD)
>>> m
USD 4.99
>>> m.sub_units
499
```

Money is immutable and supports most mathematical and logical operators.

```python
>>> m = Money('10.00', Currency.USD)
>>> m / 2
USD 5.00
>>> m + Money('3.00', Currency.USD)
USD 13.00
>>> m > Money('5.55', Currency.USD)
True
```

Money will automatically round to the correct number of decimal places for the currency.

```python
>>> m = Money('9.95', Currency.EUR)
>>> m * 0.15
EUR 1.49
>>> m = Money('10', Currency.JPY)
>>> m / 3
JPY 3
```

Money can be formatted for different locales.

```python
>>> Money('3.24', Currency.USD).format('en_US')
'$3.24'
>>> Money('9.95', Currency.EUR).format('en_UK')
'€5.56'
>>> Money('94', Currency.JPY).format('ja_JP')
'￥94'
```

Money does not support conversion between currencies and probably never will. Mathematical and logical operations between two money objects are only allowed if both objects are of the same currency. Otherwise, an error will be thrown.

Money will throw an error if you try to construct an object with an invalid amount for the currency (eg, 3.678 USD or 5.5 JPY).

For more examples, check out the test file!

## Is this the money library for me?

If you're just trying to do simple mathematical operations on money in different currencies, this library is probably perfect for you! Perhaps you're just running a store online and you need to compute sales tax.

```python
>>> subtotal = Money('9.95', Currency.USD)
>>> tax = subtotal * 0.07
>>> total = tax + subtotal
>>> subtotal.format('en_US')
'$9.95'
>>> tax.format('en_US')
'$0.70'
>>> total.format('en_US')
'$10.65'
```

All rounding will be done correctly, and you can open up in multiple countries with ease!

If you're doing complicated money operations that require many digits of precision for some reason (or you're running a gas station and charging that extra nine tenths of a cent), this library is not for you.

A word of warning: rounding is performed after each multiplication or division operation. While this is exactly what you want when computing sales tax, it may cause confusion if you're not expecting it.

```python
>>> m = Money('9.95', Currency.USD)
>>> m * 0.5 * 2
USD 9.96
>>> m * (0.5 * 2)
USD 9.95
>>> m * 1
USD 9.95
```

To avoid confusion, make sure you simplify your expressions!

## Future improvements

Foreign exchange rates will probably never be supported.


## Contributing

### How to start contributing

Pull requests are welcome! Please include tests for any behavior you add or change.

Install the development dependencies with:

```
make install-requirements
```

You can then run the tests from the root directory with:

```
make test-unit
```


This repo requires pull-request reviews for all changes on branches going to production.

### Maintainers response times

We do our best to acknowledge issues and pull requests within 5 business days.
Response times may vary depending on maintainer availability and the complexity of the request.


## Acknowledgements

This repository is based on the https://github.com/vimeo/py-money repository.

Much of the code is borrowed from https://github.com/carlospalol/money. Much of the logic for handling foreign currencies is taken from https://github.com/sebastianbergmann/money. Money formatting is powered by [Babel](http://babel.pocoo.org/).
