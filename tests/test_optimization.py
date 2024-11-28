import pytest
import pandas as pd
from optimization import optimize_parameters, get_best_parameters

def test_optimize_parameters():
    """Test optimization with a simple range of parameters."""
    data = pd.DataFrame({
        'close': [100, 110, 105, 120, 115]
    })
    
    # Simple parameter ranges for testing
    ema_short_range = range(5, 10, 5)
    ema_long_range = range(10, 15, 5)
    rsi_range = range(10, 20, 10)
    rsi_oversold_range = range(20, 30, 10)
    rsi_overbought_range = range(70, 80, 10)

    results_df = optimize_parameters(data, ema_short_range, ema_long_range, rsi_range, rsi_oversold_range, rsi_overbought_range)
    assert not results_df.empty, "Optimization results should not be empty."

def test_get_best_parameters():
    """Test getting the best parameters from optimization results."""
    results_df = pd.DataFrame({
        'Short EMA': [5, 6, 7],
        'Long EMA': [10, 12, 14],
        'RSI Period': [14, 16, 18],
        'RSI Oversold': [30, 40, 50],
        'RSI Overbought': [70, 75, 80],
        'Final Portfolio Value': [1000, 1100, 1200]
    })
    
    best_params = get_best_parameters(results_df)
    assert best_params['Final Portfolio Value'] == 1200, "The best parameter set should have the highest final value."
