"""
TradeScope Usage Examples
Example scripts demonstrating various use cases for the TradeScope toolkit.
"""

# Example 1: Basic Analysis
# Analyze a single product-market combination
from src.pipeline import TradeScopePipeline

def basic_analysis():
    """Basic single market analysis."""
    pipeline = TradeScopePipeline()

    # Analyze women's apparel in EU market
    report = pipeline.analyze(
        product="women-apparel",
        market="EU",
        output="text"
    )
    print(report)


# Example 2: Market Comparison
# Compare a product across multiple markets
def compare_markets():
    """Compare a product across all available markets."""
    pipeline = TradeScopePipeline()

    # Compare electronics across specific markets
    result = pipeline.compare_markets(
        product="electronics",
        markets=["EU", "US", "SE-Asia", "Middle-East"]
    )

    # Print rankings
    print("Market Rankings for Electronics:")
    print("-" * 50)
    for ranking in result["comparison"]["rankings"]:
        print(f"#{ranking['rank']}: {ranking['market']}")
        print(f"    Score: {ranking['score']}/100")
        print(f"    Margin: {ranking['margin']*100:.1f}%")
        print(f"    {ranking['recommendation']}")
        print()


# Example 3: JSON Output
# Get structured data for programmatic use
def json_analysis():
    """Get analysis results in JSON format."""
    pipeline = TradeScopePipeline()

    # Get JSON output
    json_report = pipeline.analyze(
        product="home-textiles",
        market="SE-Asia",
        output="json"
    )
    print(json_report)

    # Parse JSON for further processing
    import json
    data = json.loads(json_report)
    print(f"\nMarket Score: {data['financials']['market_attractiveness_score']}")
    print(f"Recommendation: {data['recommendation']}")


# Example 4: HTML Report Generation
# Generate a styled HTML report
def html_report():
    """Generate HTML report for web viewing."""
    pipeline = TradeScopePipeline()

    report = pipeline.analyze(
        product="plus-size-fashion",
        market="US",
        output="html"
    )

    # Save to file
    with open("market_report.html", "w", encoding="utf-8") as f:
        f.write(report)

    print("HTML report saved to: market_report.html")


# Example 5: Using Individual Agents
# Access agents directly for more control
def individual_agents():
    """Use agents individually for custom workflows."""
    from src.agents import DataCollectionAgent, AnalysisAgent, IntelligenceAgent

    # Step 1: Collect data
    collection_agent = DataCollectionAgent()
    data = collection_agent.collect("women-apparel", "EU")

    # Step 2: Analyze (custom scoring)
    analysis_agent = AnalysisAgent()
    analysis_agent.weights = {
        "tariff": 0.4,   # Increase tariff weight
        "demand": 0.3,
        "risk": 0.3,
    }
    analysis = analysis_agent.analyze(data)

    # Step 3: Generate report
    intelligence_agent = IntelligenceAgent()
    report = intelligence_agent.generate_report(analysis, "text")
    print(report)


# Example 6: Bulk Market Analysis
# Analyze multiple products across all markets
def bulk_analysis():
    """Analyze multiple products across all markets."""
    pipeline = TradeScopePipeline()

    products = ["women-apparel", "electronics", "home-textiles"]
    markets = pipeline.get_available_markets()

    results = []
    for product in products:
        for market in markets:
            print(f"Analyzing {product} in {market}...")
            analysis = pipeline.analyze(product, market, "json")
            import json
            results.append(json.loads(analysis))

    # Find best opportunities
    print("\n" + "=" * 60)
    print("TOP 5 MARKET OPPORTUNITIES")
    print("=" * 60)

    sorted_results = sorted(
        results,
        key=lambda x: x["financials"]["market_attractiveness_score"],
        reverse=True
    )

    for i, r in enumerate(sorted_results[:5], 1):
        print(f"\n#{i}: {r['product'].upper()} → {r['market']}")
        print(f"    Score: {r['financials']['market_attractiveness_score']}/100")
        print(f"    {r['recommendation']}")


# Example 7: List Available Options
def list_options():
    """List available markets and products."""
    pipeline = TradeScopePipeline()

    print("Available Markets:")
    for market in pipeline.get_available_markets():
        print(f"  - {market}")

    print("\nAvailable Products:")
    for product in pipeline.get_available_products():
        print(f"  - {product}")


# Run examples
if __name__ == "__main__":
    print("Example 1: Basic Analysis")
    print("=" * 60)
    basic_analysis()
