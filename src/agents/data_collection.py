"""
Data Collection Agent for TradeScope.

Collects and aggregates trade data from multiple sources.
"""

from typing import Dict, Any
from datetime import datetime

from ..config.markets import get_market, get_product


class DataCollectionAgent:
    """Agent 1: Collect and aggregate trade data from multiple sources.
    
    Attributes:
        sources: List of data source names
        last_updated: Timestamp of last data collection
    """
    
    def __init__(self, sources: list[str] = None):
        """Initialize DataCollectionAgent.
        
        Args:
            sources: List of data source names (e.g., "customs", "wtc", "un_comtrade")
        """
        self.sources = sources or ["customs", "wtc", "un_comtrade"]
        self.last_updated = None
    
    def collect(self, product: str, market: str) -> Dict[str, Any]:
        """Gather trade statistics for a product-market combination.
        
        Args:
            product: Product category name
            market: Target market region
            
        Returns:
            Dictionary of collected trade data
        """
        product_info = get_product(product) or {"hs_codes": ["0000"], "avg_margin": 0.30}
        market_info = get_market(market)
        
        if market_info is None:
            from ..config.markets import MarketInfo
            market_info = MarketInfo(market, "Unknown", 10.0, 50.0, "Unknown", 0.5)
        
        data = {
            "product": product,
            "market": market,
            "hs_codes": product_info["hs_codes"],
            "avg_margin": product_info["avg_margin"],
            "tariff_rate": market_info.tariff_rate,
            "demand_index": market_info.demand_index,
            "competition_level": market_info.competition_level,
            "risk_score": market_info.risk_score,
            "collected_at": datetime.now().isoformat(),
            "sources": self.sources,
        }
        self.last_updated = data["collected_at"]
        print(f"[DataCollection] Collected data for {product} in {market}")
        return data
    
    def collect_multi_market(self, product: str) -> Dict[str, Dict[str, Any]]:
        """Collect data for a product across all markets.
        
        Args:
            product: Product category name
            
        Returns:
            Dictionary mapping market names to trade data
        """
        from ..config.markets import list_markets
        results = {}
        for market in list_markets():
            results[market] = self.collect(product, market)
        return results
