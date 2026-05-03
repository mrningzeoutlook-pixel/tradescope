"""
Pytest configuration and fixtures for TradeScope tests.
"""

import pytest
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.agents import DataCollectionAgent, AnalysisAgent, IntelligenceAgent
from src.pipeline import TradeScopePipeline


@pytest.fixture
def data_collection_agent():
    """Fixture for DataCollectionAgent."""
    return DataCollectionAgent()


@pytest.fixture
def analysis_agent():
    """Fixture for AnalysisAgent."""
    return AnalysisAgent()


@pytest.fixture
def intelligence_agent():
    """Fixture for IntelligenceAgent."""
    return IntelligenceAgent()


@pytest.fixture
def pipeline():
    """Fixture for TradeScopePipeline."""
    return TradeScopePipeline()


@pytest.fixture
def sample_data():
    """Sample collected data for testing."""
    return {
        "product": "women-apparel",
        "market": "EU",
        "market_name": "European Union",
        "market_region": "Europe",
        "hs_codes": ["6204", "6206"],
        "avg_margin": 0.45,
        "tariff_rate": 12.0,
        "demand_index": 85.0,
        "competition_level": "High",
        "risk_score": 0.3,
        "collected_at": "2024-01-01T00:00:00",
    }


@pytest.fixture
def sample_analysis():
    """Sample analysis results for testing."""
    return {
        "product": "women-apparel",
        "market": "EU",
        "market_name": "European Union",
        "market_region": "Europe",
        "hs_codes": ["6204", "6206"],
        "avg_margin": 0.45,
        "tariff_rate": 12.0,
        "demand_index": 85.0,
        "competition_level": "High",
        "risk_score": 0.3,
        "collected_at": "2024-01-01T00:00:00",
        "market_attractiveness_score": 75.5,
        "margin_after_tariff": 0.33,
        "recommendation": "Strong Buy - High potential market",
        "trend": "growing",
        "scoring_breakdown": {
            "tariff_score": 60.0,
            "demand_score": 85.0,
            "risk_score": 70.0,
        },
    }
