"""
Python wrapper for the Backpack.tf API
"""
from bptf import webcalls
from bptf.webcalls import community_prices
from bptf.webcalls import currencies
from bptf.webcalls import price_history
from bptf.webcalls import special_items
from bptf.webcalls import user_info
from bptf import settings
from bptf import exceptions
from bptf import utils

__author__ = 'Ian Doarn'
__version__ = '1.0.0'

__all__ = [
    'webcalls',
    'exceptions',
    'settings',
    'utils'
]
