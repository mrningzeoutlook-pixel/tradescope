"""
Tests for TradeScopePipeline.
"""

import pytest
from src.pipeline import TradeScopePipeline
from src.config.market_data import MARKET_DATA


class TestTradeScopePipeline:
    """Test suite for TradeScopePipeline."""

    def test_pipeline_initialization(self, pipeline):
        """Test pipeline initializes with all agents."""
        assert hasattr(pipeline, "collection_agent")
        assert hasattr(pipeline, "analysis_agent")
        assert hasattr(pipeline, "intelligence_agent")

    def test_analyze_returns_string(self, pipeline):
        """Test analyze returns a string."""
        result = pipeline.analyze("women-apparel", "EU", "text")
        assert isinstance(result, str)
        assert len(result) > 0

    def test_analyze_json_output(self, pipeline):
        """Test analyze with JSON output."""
        result = pipeline.analyze("electronics", "US", "json")
        assert "product" in result
        assert "market" in result

    def test_analyze_html_output(self, pipeline):
        """Test analyze with HTML output."""
        result = pipeline.analyze("home-textiles", "SE-Asia", "html")
        assert "<html" in result.lower()
        assert "<body>" in result.lower()

    def test_compare_markets(self, pipeline):
        """Test market comparison."""
        markets = ["EU", "US"]
        result = pipeline.compare_markets("women-apparel", markets, "text")
        assert "product" in result
        assert "comparison" in result
        assert len(result["analyses"]) == 2

    def test_compare_markets_default(self, pipeline):
        """Test compare_markets with default markets."""
        result = pipeline.compare_markets("electronics")
        assert len(result["analyses"]) > 0

    def test_compare_markets_rankings(self, pipeline):
        """Test that comparison includes rankings."""
        markets = ["EU", "US", "SE-Asia"]
        result = pipeline.compare_markets("women-apparel", markets)
        assert "rankings" in result["comparison"]
        assert len(result["comparison"]["rankings"]) == 3

    def test_compare_markets_best_market(self, pipeline):
        """Test that comparison identifies best market."""
        result = pipeline.compare_markets("electronics", ["EU", "US"])
        assert result["comparison"]["best_market"] is not None

    def test_compare_markets_summary(self, pipeline):
        """Test comparison summary statistics."""
        markets = ["EU", "US", "SE-Asia"]
        result = pipeline.compare_markets("home-textiles", markets)
        summary = result["comparison"]["summary"]
        assert "total_markets_analyzed" in summary
        assert "avg_score" in summary
        assert "avg_margin" in summary
        assert summary["total_markets_analyzed"] == 3

    def test_get_available_markets(self, pipeline):
        """Test getting available markets."""
        markets = pipeline.get_available_markets()
        assert isinstance(markets, list)
        assert len(markets) > 0
        assert "EU" in markets
        assert "US" in markets

    def test_get_available_products(self, pipeline):
        """Test getting available products."""
        products = pipeline.get_available_products()
        assert isinstance(products, list)
        assert len(products) > 0
        assert "women-apparel" in products
        assert "electronics" in products

    def test_analyze_unknown_product(self, pipeline):
        """Test analyzing unknown product category."""
        result = pipeline.analyze("unknown-category", "EU")
        assert isinstance(result, str)

    def test_analyze_unknown_market(self, pipeline):
        """Test analyzing unknown market."""
        result = pipeline.analyze("women-apparel", "UNKNOWN")
        assert isinstance(result, str)
