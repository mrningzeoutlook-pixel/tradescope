"""
Tests for utility functions.
"""

import pytest
from src.utils.formatters import (
    format_currency,
    format_percentage,
    calculate_score,
    calculate_landed_cost,
    determine_trend,
    validate_market_code,
    validate_product_category,
)


class TestFormatters:
    """Test suite for utility functions."""

    def test_format_currency_default(self):
        """Test currency formatting with default USD."""
        result = format_currency(1234.56)
        assert "$" in result
        assert "1,234.56" in result

    def test_format_currency_eur(self):
        """Test EUR formatting."""
        result = format_currency(1000.00, "EUR")
        assert "€" in result

    def test_format_currency_gbp(self):
        """Test GBP formatting."""
        result = format_currency(500.00, "GBP")
        assert "£" in result

    def test_format_percentage(self):
        """Test percentage formatting."""
        result = format_percentage(0.4567)
        assert "45.7%" in result

    def test_format_percentage_decimals(self):
        """Test percentage with specific decimals."""
        result = format_percentage(0.5, decimals=2)
        assert "50.00%" in result

    def test_format_percentage_whole(self):
        """Test percentage with 0 decimals."""
        result = format_percentage(0.3333, decimals=0)
        assert "33%" in result


class TestCalculateScore:
    """Test suite for score calculation."""

    def test_calculate_score_basic(self):
        """Test basic score calculation."""
        score = calculate_score(10.0, 80.0, 0.3)
        assert 0 <= score <= 100
        assert isinstance(score, float)

    def test_calculate_score_custom_weights(self):
        """Test score with custom weights."""
        weights = {"tariff": 0.5, "demand": 0.3, "risk": 0.2}
        score = calculate_score(15.0, 70.0, 0.4, weights)
        assert 0 <= score <= 100

    def test_calculate_score_low_tariff_better(self):
        """Test that lower tariff gives higher score."""
        low_tariff = calculate_score(5.0, 80.0, 0.3)
        high_tariff = calculate_score(20.0, 80.0, 0.3)
        assert low_tariff > high_tariff

    def test_calculate_score_high_demand_better(self):
        """Test that higher demand gives higher score."""
        high_demand = calculate_score(10.0, 90.0, 0.3)
        low_demand = calculate_score(10.0, 50.0, 0.3)
        assert high_demand > low_demand

    def test_calculate_score_low_risk_better(self):
        """Test that lower risk gives higher score."""
        low_risk = calculate_score(10.0, 80.0, 0.1)
        high_risk = calculate_score(10.0, 80.0, 0.6)
        assert low_risk > high_risk


class TestCalculateLandedCost:
    """Test suite for landed cost calculation."""

    def test_calculate_landed_cost(self):
        """Test basic landed cost calculation."""
        cost = calculate_landed_cost(100.0, 10.0)
        assert cost == 110.0

    def test_calculate_landed_cost_zero_tariff(self):
        """Test landed cost with zero tariff."""
        cost = calculate_landed_cost(100.0, 0.0)
        assert cost == 100.0

    def test_calculate_landed_cost_high_tariff(self):
        """Test landed cost with high tariff."""
        cost = calculate_landed_cost(100.0, 25.0)
        assert cost == 125.0


class TestDetermineTrend:
    """Test suite for trend determination."""

    def test_determine_trend_growing(self):
        """Test growing trend."""
        assert determine_trend(75) == "growing"
        assert determine_trend(100) == "growing"

    def test_determine_trend_stable(self):
        """Test stable trend."""
        assert determine_trend(55) == "stable"
        assert determine_trend(65) == "stable"

    def test_determine_trend_declining(self):
        """Test declining trend."""
        assert determine_trend(40) == "declining"
        assert determine_trend(10) == "declining"


class TestValidation:
    """Test suite for validation functions."""

    def test_validate_market_code_valid(self):
        """Test valid market code."""
        assert validate_market_code("EU", ["EU", "US", "SE-Asia"]) is True

    def test_validate_market_code_invalid(self):
        """Test invalid market code."""
        assert validate_market_code("UNKNOWN", ["EU", "US"]) is False

    def test_validate_product_category_valid(self):
        """Test valid product category."""
        products = ["women-apparel", "electronics", "home-textiles"]
        assert validate_product_category("electronics", products) is True

    def test_validate_product_category_invalid(self):
        """Test invalid product category."""
        products = ["women-apparel", "electronics"]
        assert validate_product_category("unknown", products) is False
