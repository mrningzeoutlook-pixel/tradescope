"""Tests for TradeScope configuration."""

import pytest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.config.markets import MARKET_DATA, PRODUCT_CATEGORIES, get_market, list_markets, MarketInfo


class TestMarketData:
    def test_eu_market(self):
        m = get_market("EU")
        assert m is not None
        assert m.tariff_rate == 12.0
        assert m.demand_index == 85.0

    def test_list_markets(self):
        markets = list_markets()
        assert "EU" in markets
        assert "US" in markets
        assert len(markets) >= 5

    def test_unknown_market(self):
        assert get_market("unknown") is None


class TestProductCategories:
    def test_plus_size_fashion(self):
        p = PRODUCT_CATEGORIES["plus-size-fashion"]
        assert "6204" in p["hs_codes"]
        assert p["avg_margin"] == 0.50
