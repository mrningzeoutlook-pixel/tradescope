"""
Analysis Agent for TradeScope.

Processes collected trade data and identifies trends.
"""

from typing import Dict, Any


class AnalysisAgent:
    """Agent 2: Analyze trade data and identify trends.
    
    Attributes:
        weights: Scoring weights for market attractiveness
    """
    
    def __init__(self, weights: Dict[str, float] = None):
        """Initialize AnalysisAgent.
        
        Args:
            weights: Custom scoring weights (default: tariff=0.3, demand=0.4, risk=0.3)
        """
        self.weights = weights or {"tariff": 0.3, "demand": 0.4, "risk": 0.3}
    
    def analyze(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Perform market analysis on collected data.
        
        Args:
            data: Collected trade data from DataCollectionAgent
            
        Returns:
            Analysis results with market scoring
        """
        tariff_impact = 1.0 - (data["tariff_rate"] / 30.0)
        demand_score = data["demand_index"] / 100.0
        risk_factor = 1.0 - data["risk_score"]
        
        market_score = (
            tariff_impact * self.weights["tariff"]
            + demand_score * self.weights["demand"]
            + risk_factor * self.weights["risk"]
        ) * 100
        
        margin_after_tariff = data["avg_margin"] - (data["tariff_rate"] / 100.0)
        
        analysis = {
            **data,
            "market_attractiveness_score": round(market_score, 1),
            "margin_after_tariff": round(margin_after_tariff, 3),
            "recommendation": self._get_recommendation(market_score, margin_after_tariff),
            "trend": "growing" if demand_score > 0.7 else "stable" if demand_score > 0.5 else "declining",
        }
        print(f"[Analysis] Market score: {market_score:.1f}/100, Recommendation: {analysis['recommendation']}")
        return analysis
    
    def _get_recommendation(self, score: float, margin: float) -> str:
        """Generate a market entry recommendation."""
        if score >= 70 and margin > 0.2:
            return "Strong Buy - High potential market"
        elif score >= 50 and margin > 0.1:
            return "Cautious Entry - Moderate opportunity"
        elif margin > 0.15:
            return "Niche Play - Selective product strategy"
        else:
            return "Avoid - Low margin or high risk"
    
    def compare_markets(self, analyses: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
        """Compare market analyses and rank them.
        
        Args:
            analyses: Dict mapping market names to analysis results
            
        Returns:
            Comparison report with rankings
        """
        ranked = sorted(
            analyses.items(),
            key=lambda x: x[1].get("market_attractiveness_score", 0),
            reverse=True,
        )
        
        return {
            "rankings": [{"market": m, "score": a["market_attractiveness_score"], "recommendation": a["recommendation"]} for m, a in ranked],
            "best_market": ranked[0][0] if ranked else None,
            "total_markets": len(ranked),
        }
