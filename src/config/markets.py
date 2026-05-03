"""
Market data configurations for TradeScope.

Defines market information, product categories, and regional trade data.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class MarketInfo:
    """Market information container.
    
    Attributes:
        country: Country or region name
        region: Geographic region
        tariff_rate: Average tariff rate (%)
        demand_index: Market demand index (0-100)
        competition_level: Competition intensity
        risk_score: Political/economic risk score (0-1)
    """
    country: str
    region: str
    tariff_rate: float
    demand_index: float
    competition_level: str
    risk_score: float


# Market data (in production, this would come from APIs)
MARKET_DATA = {
    "EU": MarketInfo("European Union", "Europe", 12.0, 85.0, "High", 0.3),
    "US": MarketInfo("United States", "North America", 16.5, 92.0, "Very High", 0.25),
    "SE-Asia": MarketInfo("Southeast Asia", "Asia-Pacific", 5.0, 78.0, "Medium", 0.4),
    "Middle-East": MarketInfo("Middle East", "MENA", 8.0, 70.0, "Low", 0.5),
    "Latin-America": MarketInfo("Latin America", "Americas", 14.0, 65.0, "Medium", 0.45),
    "Japan-Korea": MarketInfo("Japan & Korea", "Asia-Pacific", 10.0, 88.0, "High", 0.2),
    "Africa": MarketInfo("Sub-Saharan Africa", "Africa", 18.0, 55.0, "Low", 0.6),
    "CIS": MarketInfo("CIS States", "Eurasia", 9.0, 60.0, "Medium", 0.55),
}

PRODUCT_CATEGORIES = {
    "women-apparel": {"hs_codes": ["6204", "6206"], "avg_margin": 0.45},
    "plus-size-fashion": {"hs_codes": ["6204"], "avg_margin": 0.50},
    "electronics": {"hs_codes": ["8517", "8528"], "avg_margin": 0.25},
    "home-textiles": {"hs_codes": ["6302", "6304"], "avg_margin": 0.35},
    "beauty-cosmetics": {"hs_codes": ["3304", "3305"], "avg_margin": 0.60},
    "sporting-goods": {"hs_codes": ["9506"], "avg_margin": 0.40},
}


def get_market(name: str) -> Optional[MarketInfo]:
    """Get market information by name."""
    return MARKET_DATA.get(name)


def list_markets() -> list[str]:
    """List all available market names."""
    return list(MARKET_DATA.keys())


def get_product(name: str) -> Optional[dict]:
    """Get product category information by name."""
    return PRODUCT_CATEGORIES.get(name)


def list_products() -> list[str]:
    """List all available product categories."""
    return list(PRODUCT_CATEGORIES.keys())
