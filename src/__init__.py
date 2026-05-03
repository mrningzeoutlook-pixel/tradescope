"""
TradeScope - International Trade Data Analysis & Market Intelligence Toolkit

Analyze markets, compare tariffs, and generate actionable trade insights.
"""

__version__ = "0.2.0"
__author__ = "Mary Ma"
__email__ = "mary@tradescope.ai"
__license__ = "MIT"

from .pipeline import TradeScopePipeline
from .config.markets import MARKET_DATA, PRODUCT_CATEGORIES, MarketInfo

__all__ = [
    "TradeScopePipeline",
    "MARKET_DATA",
    "PRODUCT_CATEGORIES",
    "MarketInfo",
]
