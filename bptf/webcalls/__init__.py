"""
Web Calls

Collection of web calls that can be made to the API
"""
from . import community_prices
from . import currencies
from . import price_history
from . import special_items
from . import user_info

__all__ = [
    'community_prices',
    'currencies',
    'price_history',
    'special_items',
    'user_info'
]
