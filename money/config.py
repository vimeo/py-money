"""Money config"""

from decimal import ROUND_HALF_UP

def _get_base_config():
    """
    Extensible configuration for the ``Money`` class.
    Keys supported:
    ``rounding_per_operation``, bool, whether to apply the ``_round`` function
    after certain operations (i.e. multiplication, division).
    ``rounding_type``, if ``rounding_per_operation`` is set, which kind of rounding
    should be applied after certain operations.
    """
    return {
        'rounding_per_operation': True,
        'rounding_type': ROUND_HALF_UP,
    }

MONEY_CONFIG = _get_base_config()
