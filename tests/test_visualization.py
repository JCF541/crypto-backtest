import pytest
import pandas as pd
from src.visualization import plot_portfolio_performance, save_optimization_heatmap

def test_plot_portfolio_performance():
    """Test that the portfolio performance plot runs without errors."""
    data = pd.DataFrame({
        'close': [100, 110, 120, 115, 125],
        'portfolio_value': [1000, 1100, 1200, 1150, 1250],
        'signal': [0, 1, 0, -1, 0]
    })
    plot_portfolio_performance(data)  # No exceptions = pass

def test_save_optimization_heatmap():
    """Test that the heatmap generation runs without errors."""
    results_df = pd.DataFrame({
        'RSI Period': [10, 14, 18],
        'RSI Overbought': [70, 75, 80],
        'Final Portfolio Value': [1000, 1100, 1200]
    })
    save_optimization_heatmap(results_df)  # No exceptions = pass
