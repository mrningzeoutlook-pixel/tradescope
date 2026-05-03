"""
Tests for AnalysisAgent.
"""

import pytest
from src.agents.analysis import AnalysisAgent


class TestAnalysisAgent:
    """Test suite for AnalysisAgent."""

    def test_analyze_returns_dict(self, analysis_agent, sample_data):
        """Test that analyze returns a dictionary."""
        result = analysis_agent.analyze(sample_data)
        assert isinstance(result, dict)

    def test_analyze_adds_score(self, analysis_agent, sample_data):
        """Test that analysis adds market attractiveness score."""
        result = analysis_agent.analyze(sample_data)
        assert "market_attractiveness_score" in result
        assert 0 <= result["market_attractiveness_score"] <= 100

    def test_analyze_calculates_margin(self, analysis_agent, sample_data):
        """Test that margin after tariff is calculated correctly."""
        result = analysis_agent.analyze(sample_data)
        expected_margin = sample_data["avg_margin"] - (sample_data["tariff_rate"] / 100)
        assert result["margin_after_tariff"] == pytest.approx(expected_margin, rel=0.01)

    def test_analyze_adds_recommendation(self, analysis_agent, sample_data):
        """Test that recommendation is added."""
        result = analysis_agent.analyze(sample_data)
        assert "recommendation" in result
        assert isinstance(result["recommendation"], str)

    def test_analyze_adds_trend(self, analysis_agent, sample_data):
        """Test that trend is determined correctly."""
        result = analysis_agent.analyze(sample_data)
        assert "trend" in result
        assert result["trend"] in ["growing", "stable", "declining"]

    def test_analyze_high_demand_growing(self, analysis_agent, sample_data):
        """Test growing trend for high demand."""
        sample_data["demand_index"] = 80.0
        result = analysis_agent.analyze(sample_data)
        assert result["trend"] == "growing"

    def test_analyze_medium_demand_stable(self, analysis_agent, sample_data):
        """Test stable trend for medium demand."""
        sample_data["demand_index"] = 60.0
        result = analysis_agent.analyze(sample_data)
        assert result["trend"] == "stable"

    def test_analyze_low_demand_declining(self, analysis_agent, sample_data):
        """Test declining trend for low demand."""
        sample_data["demand_index"] = 40.0
        result = analysis_agent.analyze(sample_data)
        assert result["trend"] == "declining"

    def test_analyze_adds_scoring_breakdown(self, analysis_agent, sample_data):
        """Test that scoring breakdown is included."""
        result = analysis_agent.analyze(sample_data)
        assert "scoring_breakdown" in result
        breakdown = result["scoring_breakdown"]
        assert "tariff_score" in breakdown
        assert "demand_score" in breakdown
        assert "risk_score" in breakdown

    def test_compare_markets(self, analysis_agent):
        """Test comparing multiple market analyses."""
        analysis_results = [
            {
                "market": "EU",
                "market_name": "European Union",
                "market_attractiveness_score": 75.0,
                "margin_after_tariff": 0.33,
                "recommendation": "Strong Buy",
            },
            {
                "market": "US",
                "market_name": "United States",
                "market_attractiveness_score": 80.0,
                "margin_after_tariff": 0.28,
                "recommendation": "Strong Buy",
            },
        ]
        comparison = analysis_agent.compare_markets(analysis_results)
        assert "rankings" in comparison
        assert "best_market" in comparison
        assert len(comparison["rankings"]) == 2
        # US should be ranked first (higher score)
        assert comparison["rankings"][0]["market"] == "US"

    def test_compare_markets_empty(self, analysis_agent):
        """Test compare_markets with empty list."""
        comparison = analysis_agent.compare_markets([])
        assert comparison["rankings"] == []
        assert comparison["best_market"] is None

    def test_recommendation_strong_buy(self, analysis_agent):
        """Test strong buy recommendation criteria."""
        rec = analysis_agent._get_recommendation(75.0, 0.25)
        assert "Strong Buy" in rec

    def test_recommendation_cautious_entry(self, analysis_agent):
        """Test cautious entry recommendation criteria."""
        rec = analysis_agent._get_recommendation(55.0, 0.15)
        assert "Cautious Entry" in rec

    def test_recommendation_niche_play(self, analysis_agent):
        """Test niche play recommendation criteria."""
        rec = analysis_agent._get_recommendation(45.0, 0.20)
        assert "Niche Play" in rec

    def test_recommendation_avoid(self, analysis_agent):
        """Test avoid recommendation criteria."""
        rec = analysis_agent._get_recommendation(40.0, 0.05)
        assert "Avoid" in rec

    def test_weights_configuration(self, analysis_agent):
        """Test that scoring weights are configurable."""
        assert analysis_agent.weights["tariff"] == 0.30
        assert analysis_agent.weights["demand"] == 0.40
        assert analysis_agent.weights["risk"] == 0.30
