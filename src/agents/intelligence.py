"""
Intelligence Agent for TradeScope.

Generates actionable market intelligence reports.
"""

from typing import Dict, Any
import json


class IntelligenceAgent:
    """Agent 3: Generate actionable market intelligence report.
    
    Attributes:
        default_format: Default output format
    """
    
    def __init__(self, default_format: str = "text"):
        """Initialize IntelligenceAgent.
        
        Args:
            default_format: Default report format (text, json, html)
        """
        self.default_format = default_format
    
    def generate_report(self, analysis: Dict[str, Any], output_format: str = None) -> str:
        """Generate a formatted market intelligence report.
        
        Args:
            analysis: Analysis results from AnalysisAgent
            output_format: Output format (text, json, html)
            
        Returns:
            Formatted report string
        """
        output_format = output_format or self.default_format
        
        if output_format == "json":
            return json.dumps(analysis, indent=2, ensure_ascii=False)
        elif output_format == "html":
            return self._generate_html(analysis)
        else:
            return self._generate_text(analysis)
    
    def _generate_text(self, analysis: Dict[str, Any]) -> str:
        """Generate text format report."""
        separator = "=" * 60
        return f"""
{separator}
  TRADESCOPE MARKET INTELLIGENCE REPORT
{separator}

  Product:      {analysis['product'].upper()}
  Market:       {analysis['market']}
  HS Codes:     {', '.join(analysis['hs_codes'])}

  --- Market Metrics ---
  Demand Index:     {analysis['demand_index']}/100 ({analysis['trend']})
  Tariff Rate:      {analysis['tariff_rate']}%
  Competition:      {analysis['competition_level']}
  Risk Score:       {analysis['risk_score']}/1.0

  --- Financial Analysis ---
  Avg Margin:       {analysis['avg_margin']*100:.1f}%
  Margin After Tax: {analysis['margin_after_tariff']*100:.1f}%
  Market Score:     {analysis['market_attractiveness_score']}/100

  --- Recommendation ---
  {analysis['recommendation']}

{separator}
  Report generated: {analysis['collected_at']}
{separator}
"""
    
    def _generate_html(self, analysis: Dict[str, Any]) -> str:
        """Generate HTML format report."""
        return f"""<!DOCTYPE html>
<html><head><title>TradeScope Report - {analysis['product']}</title>
<style>body{{font-family:sans-serif;max-width:800px;margin:auto;padding:20px}}
table{{border-collapse:collapse;width:100%}}td,th{{border:1px solid #ddd;padding:8px;text-align:left}}</style>
</head><body>
<h1>TradeScope Market Intelligence Report</h1>
<table><tr><th>Metric</th><th>Value</th></tr>
<tr><td>Product</td><td>{analysis['product']}</td></tr>
<tr><td>Market</td><td>{analysis['market']}</td></tr>
<tr><td>Tariff Rate</td><td>{analysis['tariff_rate']}%</td></tr>
<tr><td>Demand Index</td><td>{analysis['demand_index']}/100</td></tr>
<tr><td>Market Score</td><td>{analysis['market_attractiveness_score']}/100</td></tr>
<tr><td>Recommendation</td><td><strong>{analysis['recommendation']}</strong></td></tr>
</table></body></html>"""
