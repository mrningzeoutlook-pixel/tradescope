"""Configuration package for TradeScope."""

from .markets import MarketInfo, MARKET_DATA, PRODUCT_CATEGORIES, get_market, list_markets, get_product, list_products

__all__ = [
    "MarketInfo", "MARKET_DATA", "PRODUCT_CATEGORIES",
    "get_market", "list_markets", "get_product", "list_products",
]
