"""
Tests for IntelligenceAgent.
"""

import pytest
import json
from src.agents.intelligence import IntelligenceAgent


class TestIntelligenceAgent:
    """Test suite for IntelligenceAgent."""

    def test_generate_report_text(self, intelligence_agent, sample_analysis):
        """Test text report generation."""
        result = intelligence_agent.generate_report(sample_analysis, "text")
        assert isinstance(result, str)
        assert "TRADESCOPE" in result or "tradescope" in result.lower()

    def test_generate_report_json(self, intelligence_agent, sample_analysis):
        """Test JSON report generation."""
        result = intelligence_agent.generate_report(sample_analysis, "json")
        assert isinstance(result, str)
        # Verify it's valid JSON
        parsed = json.loads(result)
        assert "product" in parsed
        assert "market" in parsed
        assert "metrics" in parsed

    def test_generate_report_html(self, intelligence_agent, sample_analysis):
        """Test HTML report generation."""
        result = intelligence_agent.generate_report(sample_analysis, "html")
        assert isinstance(result, str)
        assert "<html" in result.lower()
        assert "<body>" in result.lower()
        assert "DOCTYPE" in result

    def test_generate_report_default_format(self, intelligence_agent, sample_analysis):
        """Test default output format is text."""
        result = intelligence_agent.generate_report(sample_analysis)
        assert isinstance(result, str)

    def test_json_report_structure(self, intelligence_agent, sample_analysis):
        """Test JSON report has correct structure."""
        result = intelligence_agent.generate_report(sample_analysis, "json")
        parsed = json.loads(result)
        assert parsed["report_type"] == "Market Intelligence Report"
        assert parsed["version"] == "1.0"
        assert "product" in parsed
        assert "market" in parsed
        assert "metrics" in parsed
        assert "financials" in parsed
        assert "recommendation" in parsed

    def test_html_report_contains_data(self, intelligence_agent, sample_analysis):
        """Test HTML report contains key data points."""
        result = intelligence_agent.generate_report(sample_analysis, "html")
        assert str(sample_analysis["market_attractiveness_score"]) in result
        assert sample_analysis["product"].upper() in result

    def test_generate_summary(self, intelligence_agent, sample_analysis):
        """Test summary generation."""
        summary = intelligence_agent.generate_summary(sample_analysis)
        assert isinstance(summary, str)
        assert sample_analysis["market"] in summary
        assert sample_analysis["recommendation"] in summary

    def test_text_report_separator(self, intelligence_agent, sample_analysis):
        """Test that text report contains separator."""
        result = intelligence_agent.generate_report(sample_analysis, "text")
        assert "=" in result  # Separator character

    def test_invalid_format_defaults_to_text(self, intelligence_agent, sample_analysis):
        """Test that invalid format defaults to text."""
        result = intelligence_agent.generate_report(sample_analysis, "invalid")
        assert isinstance(result, str)

    def test_recommendation_class_in_html(self, intelligence_agent):
        """Test HTML recommendation class is correctly set."""
        # Strong buy
        strong_analysis = {**sample_analysis, "recommendation": "Strong Buy - High potential market"}
        result = intelligence_agent.generate_report(strong_analysis, "html")
        assert "recommendation-strong" in result

        # Cautious
        cautious_analysis = {**sample_analysis, "recommendation": "Cautious Entry - Moderate opportunity"}
        result = intelligence_agent.generate_report(cautious_analysis, "html")
        assert "recommendation-moderate" in result

    def test_trend_indicator_in_html(self, intelligence_agent, sample_analysis):
        """Test HTML report shows trend indicator."""
        result = intelligence_agent.generate_report(sample_analysis, "html")
        # Should show trend icon
        assert "growing" in result or "stable" in result or "declining" in result
