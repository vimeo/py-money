"""Currency tests"""

from money.currency import Currency

# pylint: disable=no-self-use,missing-docstring


class TestCurrency:
    """Currency tests"""

    def test_currency_fields(self):
        currency = Currency.AED
        assert currency.name == "AED"
        assert currency.value == "AED"
        assert currency.display_name == "UAE Dirham"
        assert currency.numeric_code == 784
        assert currency.default_fraction_digits == 2
        assert currency.sub_unit == 100

    def test_currency_symbol(self):
        currency = Currency.USD
        assert currency.symbol() == "$"
        assert currency.symbol("en_US") == "$"
        assert currency.symbol("en_GB") == "US$"
        assert currency.symbol("es_MX") == "USD"
