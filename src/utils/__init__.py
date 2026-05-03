"""Utilities for TradeScope."""

import os


def ensure_dir(path: str) -> str:
    abs_path = os.path.abspath(path)
    os.makedirs(abs_path, exist_ok=True)
    return abs_path


def format_tariff(rate: float) -> str:
    return f"{rate:.1f}%"


def format_margin(margin: float) -> str:
    return f"{margin*100:.1f}%"
