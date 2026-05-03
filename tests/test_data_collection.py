"""
Tests for DataCollectionAgent.
"""

import pytest
from src.agents.data_collection import DataCollectionAgent, MarketInfo


class TestDataCollectionAgent:
    """Test suite for DataCollectionAgent."""

    def test_collect_returns_dict(self, data_collection_agent):
        """Test that collect returns a dictionary."""
        result = data_collection_agent.collect("women-apparel", "EU")
        assert isinstance(result, dict)

    def test_collect_contains_required_fields(self, data_collection_agent):
        """Test that collected data contains all required fields."""
        result = data_collection_agent.collect("electronics", "US")
        required_fields = [
            "product", "market", "hs_codes", "avg_margin",
            "tariff_rate", "demand_index", "competition_level",
            "risk_score", "collected_at"
        ]
        for field in required_fields:
            assert field in result, f"Missing field: {field}"

    def test_collect_validates_product(self, data_collection_agent):
        """Test that collect handles unknown products."""
        result = data_collection_agent.collect("unknown-product", "EU")
        assert result["product"] == "unknown-product"
        assert result["hs_codes"] == ["0000"]
        assert result["avg_margin"] == 0.30

    def test_collect_validates_market(self, data_collection_agent):
        """Test that collect handles unknown markets."""
        result = data_collection_agent.collect("women-apparel", "Unknown-Market")
        assert result["market"] == "Unknown-Market"
        assert result["tariff_rate"] == 10.0
        assert result["demand_index"] == 50.0

    def test_collect_multiple_markets(self, data_collection_agent):
        """Test collecting data across multiple markets."""
        markets = ["EU", "US", "SE-Asia"]
        results = data_collection_agent.collect_multiple_markets("women-apparel", markets)
        assert len(results) == 3
        assert all(r["product"] == "women-apparel" for r in results)

    def test_collect_multiple_markets_defaults(self, data_collection_agent):
        """Test collect_multiple_markets with default markets."""
        results = data_collection_agent.collect_multiple_markets("electronics")
        assert len(results) > 0

    def test_collected_at_is_timestamp(self, data_collection_agent):
        """Test that collected_at is a valid ISO timestamp."""
        result = data_collection_agent.collect("women-apparel", "EU")
        assert "collected_at" in result
        assert "T" in result["collected_at"]  # ISO format indicator

    def test_market_info_dataclass(self):
        """Test MarketInfo dataclass creation."""
        info = MarketInfo(
            country="Test Country",
            region="Test Region",
            tariff_rate=10.0,
            demand_index=80.0,
            competition_level="Medium",
            risk_score=0.4
        )
        assert info.country == "Test Country"
        assert info.tariff_rate == 10.0
