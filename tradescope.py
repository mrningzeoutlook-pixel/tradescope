"""
TradeScope CLI Entry Point
Command-line interface for the TradeScope toolkit.
"""

import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import argparse
from src.pipeline import TradeScopePipeline
from src.config.market_data import MARKET_DATA, PRODUCT_CATEGORIES


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="TradeScope - International Trade Intelligence Toolkit",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Analyze a specific market
  python tradescope.py analyze --product "women-apparel" --market "EU"

  # Compare across all markets
  python tradescope.py compare --product "electronics"

  # Generate JSON output
  python tradescope.py analyze --product "home-textiles" --market "US" --output json

  # Generate HTML report
  python tradescope.py analyze --product "plus-size-fashion" --market "SE-Asia" --output html

Available Markets:
  EU, US, SE-Asia, Middle-East, Latin-America

Available Products:
  women-apparel, plus-size-fashion, electronics, home-textiles
        """
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # Analyze command
    analyze_parser = subparsers.add_parser("analyze", help="Analyze a specific market")
    analyze_parser.add_argument("--product", required=True, help="Product category")
    analyze_parser.add_argument("--market", default="EU", help="Target market region")
    analyze_parser.add_argument(
        "--output", default="text", choices=["text", "json", "html"],
        help="Output format"
    )
    analyze_parser.add_argument("--save", help="Save output to file")

    # Compare command
    compare_parser = subparsers.add_parser("compare", help="Compare across markets")
    compare_parser.add_argument("--product", required=True, help="Product category")
    compare_parser.add_argument(
        "--markets",
        help="Comma-separated market codes (default: all markets)"
    )
    compare_parser.add_argument(
        "--output", default="text", choices=["text", "json", "html"],
        help="Output format"
    )

    # List command
    list_parser = subparsers.add_parser("list", help="List available options")
    list_parser.add_argument(
        "--type", choices=["markets", "products"], default="markets",
        help="Type to list"
    )

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    pipeline = TradeScopePipeline()

    # Handle list command
    if args.command == "list":
        if args.type == "markets":
            print("Available Markets:")
            print("-" * 40)
            for code, info in MARKET_DATA.items():
                print(f"  {code:15} - {info.country} ({info.region})")
        else:
            print("Available Products:")
            print("-" * 40)
            for code, info in PRODUCT_CATEGORIES.items():
                print(f"  {code:20} - {info.get('description', '')}")
        return

    # Handle analyze command
    if args.command == "analyze":
        report = pipeline.analyze(args.product, args.market, args.output)

        if args.save:
            output_path = os.path.join(os.getcwd(), args.save)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(report)
            print(f"\nReport saved to: {output_path}")
        else:
            print(report)

    # Handle compare command
    elif args.command == "compare":
        markets = args.markets.split(",") if args.markets else None
        result = pipeline.compare_markets(args.product, markets, args.output)

        print("\n" + "=" * 60)
        print("MARKET COMPARISON RANKINGS")
        print("=" * 60)

        for ranking in result["comparison"]["rankings"]:
            print(f"\n#{ranking['rank']} - {ranking['market']} ({ranking['market_name']})")
            print(f"   Score: {ranking['score']}/100 | Margin: {ranking['margin']*100:.1f}%")
            print(f"   {ranking['recommendation']}")

        print("\n" + "=" * 60)
        print("SUMMARY")
        print("=" * 60)
        summary = result["comparison"]["summary"]
        print(f"  Markets Analyzed: {summary['total_markets_analyzed']}")
        print(f"  Average Score: {summary['avg_score']:.1f}/100")
        print(f"  Average Margin: {summary['avg_margin']*100:.1f}%")


if __name__ == "__main__":
    main()
