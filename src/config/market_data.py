"""
Market Data Configuration
市场数据配置，包含各地区的市场信息和产品分类
Market data definitions for trade analysis.
"""

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class MarketInfo:
    """Market information container / 市场信息"""
    country: str          # Full country name
    region: str           # Geographic region
    tariff_rate: float   # Import tariff rate (%)
    demand_index: float  # Market demand score (0-100)
    competition_level: str  # Competition intensity
    risk_score: float    # Risk assessment score (0-1)


# Market data by region code
# In production, this would be fetched from external APIs or databases
MARKET_DATA: Dict[str, MarketInfo] = {
    "EU": MarketInfo(
        country="European Union",
        region="Europe",
        tariff_rate=12.0,
        demand_index=85.0,
        competition_level="High",
        risk_score=0.3,
    ),
    "US": MarketInfo(
        country="United States",
        region="North America",
        tariff_rate=16.5,
        demand_index=92.0,
        competition_level="Very High",
        risk_score=0.25,
    ),
    "SE-Asia": MarketInfo(
        country="Southeast Asia",
        region="Asia-Pacific",
        tariff_rate=5.0,
        demand_index=78.0,
        competition_level="Medium",
        risk_score=0.4,
    ),
    "Middle-East": MarketInfo(
        country="Middle East",
        region="MENA",
        tariff_rate=8.0,
        demand_index=70.0,
        competition_level="Low",
        risk_score=0.5,
    ),
    "Latin-America": MarketInfo(
        country="Latin America",
        region="Americas",
        tariff_rate=14.0,
        demand_index=65.0,
        competition_level="Medium",
        risk_score=0.45,
    ),
}

# Product categories with HS codes and typical margins
PRODUCT_CATEGORIES: Dict[str, Dict] = {
    "women-apparel": {
        "hs_codes": ["6204", "6206"],
        "avg_margin": 0.45,
        "description": "Women's clothing and apparel",
    },
    "plus-size-fashion": {
        "hs_codes": ["6204"],
        "avg_margin": 0.50,
        "description": "Plus-size fashion clothing",
    },
    "electronics": {
        "hs_codes": ["8517", "8528"],
        "avg_margin": 0.25,
        "description": "Electronic devices and components",
    },
    "home-textiles": {
        "hs_codes": ["6302", "6304"],
        "avg_margin": 0.35,
        "description": "Home textile products (linens, curtains, etc.)",
    },
}

# Supported export formats
SUPPORTED_FORMATS = ["text", "json", "html"]

# API Configuration (for future external API integration)
API_CONFIG = {
    "default_timeout": 30,
    "retry_attempts": 3,
    "cache_ttl": 3600,  # seconds
}

# Scoring weights for market analysis
SCORING_WEIGHTS = {
    "tariff": 0.30,
    "demand": 0.40,
    "risk": 0.30,
}

# Recommendation thresholds
RECOMMENDATION_THRESHOLDS = {
    "strong_buy": {"min_score": 70, "min_margin": 0.2},
    "cautious_entry": {"min_score": 50, "min_margin": 0.1},
    "niche_play": {"min_margin": 0.15},
}
