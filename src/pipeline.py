"""
Main Pipeline for TradeScope.

Coordinates all agents for trade data analysis and intelligence generation.
"""

from typing import Dict, Any, List, Optional
import os
import json

from .agents import DataCollectionAgent, AnalysisAgent, IntelligenceAgent
from .config.markets import list_markets, get_market


class TradeScopePipeline:
    """Main pipeline orchestrating all agents for trade intelligence.
    
    Attributes:
        collection_agent: Agent for data collection
        analysis_agent: Agent for market analysis
        intelligence_agent: Agent for report generation
    """
    
    def __init__(self):
        self.collection_agent = DataCollectionAgent()
        self.analysis_agent = AnalysisAgent()
        self.intelligence_agent = IntelligenceAgent()
    
    def analyze(self, product: str, market: str, output: str = "text") -> str:
        """Run the full TradeScope analysis pipeline.
        
        Args:
            product: Product category to analyze
            market: Target market region
            output: Output format (text, json, html)
            
        Returns:
            Formatted market intelligence report
        """
        print("\n" + "=" * 60)
        print("TradeScope - Market Intelligence Pipeline")
        print("=" * 60 + "\n")
        
        data = self.collection_agent.collect(product, market)
        analysis = self.analysis_agent.analyze(data)
        report = self.intelligence_agent.generate_report(analysis, output)
        
        return report
    
    def compare(self, product: str, output: str = "text") -> Dict[str, Any]:
        """Compare a product across all markets.
        
        Args:
            product: Product category to analyze
            output: Output format
            
        Returns:
            Comparison results with rankings
        """
        analyses = {}
        for market in list_markets():
            data = self.collection_agent.collect(product, market)
            analyses[market] = self.analysis_agent.analyze(data)
        
        comparison = self.analysis_agent.compare_markets(analyses)
        
        print(f"\n[Compare] Best market for {product}: {comparison['best_market']}")
        for rank in comparison["rankings"]:
            print(f"  {rank['market']}: {rank['score']}/100 - {rank['recommendation']}")
        
        return comparison
    
    def get_supported_markets(self) -> List[str]:
        """Get list of supported markets."""
        return list_markets()
