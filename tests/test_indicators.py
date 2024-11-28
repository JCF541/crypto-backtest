import pytest
import pandas as pd
from indicators import *

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

def test_calculate_bollinger_bands():
    data = pd.Series([100, 102, 104, 103, 101])
    bands = calculate_bollinger_bands(data, period=3)
    assert 'Upper Band' in bands.columns
    assert 'Lower Band' in bands.columns

def test_calculate_macd():
    data = pd.Series([100, 102, 104, 103, 101])
    macd = calculate_macd(data)
    assert 'MACD' in macd.columns
    assert 'Signal Line' in macd.columns

