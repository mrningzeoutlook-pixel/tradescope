"""
Utility Functions
格式化工具和辅助函数
Helper functions for formatting and data processing.
"""


def format_currency(value: float, currency: str = "USD") -> str:
    """
    Format a value as currency.

    Args:
        value: Numeric value
        currency: Currency code (default: USD)

    Returns:
        Formatted currency string
    """
    symbols = {
        "USD": "$",
        "EUR": "€",
        "GBP": "£",
        "CNY": "¥",
    }
    symbol = symbols.get(currency, currency + " ")
    return f"{symbol}{value:,.2f}"


def format_percentage(value: float, decimals: int = 1) -> str:
    """
    Format a decimal value as percentage.

    Args:
        value: Decimal value (e.g., 0.45 for 45%)
        decimals: Number of decimal places

    Returns:
        Formatted percentage string
    """
    return f"{value * 100:.{decimals}f}%"


def calculate_score(
    tariff_rate: float,
    demand_index: float,
    risk_score: float,
    weights: dict = None
) -> float:
    """
    Calculate market attractiveness score.

    Args:
        tariff_rate: Import tariff rate (%)
        demand_index: Market demand (0-100)
        risk_score: Risk score (0-1)
        weights: Optional scoring weights dict

    Returns:
        Market attractiveness score (0-100)
    """
    if weights is None:
        weights = {"tariff": 0.30, "demand": 0.40, "risk": 0.30}

    tariff_score = 1.0 - (tariff_rate / 30.0)
    demand_score = demand_index / 100.0
    risk_factor = 1.0 - risk_score

    score = (
        tariff_score * weights["tariff"] +
        demand_score * weights["demand"] +
        risk_factor * weights["risk"]
    ) * 100

    return round(score, 1)


def calculate_landed_cost(base_cost: float, tariff_rate: float) -> float:
    """
    Calculate landed cost including tariffs.

    Args:
        base_cost: Product base cost
        tariff_rate: Tariff rate (%)

    Returns:
        Total landed cost
    """
    return base_cost * (1 + tariff_rate / 100)


def determine_trend(demand_index: float) -> str:
    """
    Determine market trend based on demand index.

    Args:
        demand_index: Demand score (0-100)

    Returns:
        Trend indicator: "growing", "stable", or "declining"
    """
    if demand_index > 70:
        return "growing"
    elif demand_index > 50:
        return "stable"
    else:
        return "declining"


def validate_market_code(code: str, available_markets: list) -> bool:
    """
    Validate if a market code is valid.

    Args:
        code: Market code to validate
        available_markets: List of valid market codes

    Returns:
        True if valid, False otherwise
    """
    return code in available_markets


def validate_product_category(category: str, available_products: list) -> bool:
    """
    Validate if a product category is valid.

    Args:
        category: Product category to validate
        available_products: List of valid categories

    Returns:
        True if valid, False otherwise
    """
    return category in available_products
