"""
TradeScope Setup Configuration
Python package installation and distribution settings.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README for long description
readme_file = Path(__file__).parent / "README.md"
long_description = readme_file.read_text(encoding="utf-8") if readme_file.exists() else ""

setup(
    name="tradescope",
    version="0.2.0",
    author="Mary Ma",
    author_email="mary@example.com",
    description="International Trade Data Analysis & Market Intelligence Toolkit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mrningzeoutlook-pixel/tradescope",
    project_urls={
        "Bug Tracker": "https://github.com/mrningzeoutlook-pixel/tradescope/issues",
        "Documentation": "https://github.com/mrningzeoutlook-pixel/tradescope#readme",
        "Source Code": "https://github.com/mrningzeoutlook-pixel/tradescope",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Business",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Office/Business",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages(exclude=["tests", "tests.*", "examples", "docs"]),
    package_data={
        "tradescope": ["py.typed"],
    },
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=[
        "python-dotenv>=1.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "pytest-mock>=3.10.0",
            "black>=23.0.0",
            "isort>=5.12.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
        "docker": [
            "docker>=6.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "tradescope=tradescope.cli:main",
        ],
    },
    keywords=[
        "trade",
        "market-intelligence",
        "tariff",
        "international-trade",
        "market-analysis",
        "hs-code",
        "export",
        "import",
        "cross-border",
    ],
    zip_safe=False,
)
