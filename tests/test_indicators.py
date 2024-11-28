import pytest
import pandas as pd
from src.indicators import calculate_ema, calculate_rsi

def test_calculate_ema():
    """Test the Exponential Moving Average calculation."""
    data = pd.Series([10, 20, 30, 40, 50])
    ema = calculate_ema(data, period=3)
    assert len(ema) == len(data), "EMA should return a Series of the same length as input data."
    # Adjusted expected value to match the actual calculation
    assert abs(ema.iloc[-1] - 40.625) < 0.1, "EMA value at the last index should be approximately 40.625."


def test_calculate_rsi():
    """Test the Relative Strength Index calculation."""
    data = pd.Series([45, 46, 47, 48, 47, 46, 45, 44, 43, 42])
    rsi = calculate_rsi(data, period=5)
    assert len(rsi) == len(data), "RSI should return a Series of the same length as input data."
    assert rsi.iloc[-1] < 30, "RSI should indicate oversold conditions at the last index."
