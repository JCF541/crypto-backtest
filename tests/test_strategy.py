import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from strategy import macd_strategy

def test_generate_signals():
    """Test trading signal generation."""
    data = pd.DataFrame({
        'close': [100, 105, 110, 115, 120, 125, 130, 135, 140, 145]
    })
    signals = generate_signals(data, short_ema_period=3, long_ema_period=5, rsi_period=2, rsi_overbought=80, rsi_oversold=20)
    assert 'signal' in signals.columns, "Signal column should be present in DataFrame."

def test_bollinger_band_strategy():
    data = pd.DataFrame({'Close': [100, 102, 104, 103, 101]})
    results = bollinger_band_strategy(data)
    assert 'Signal' in results.columns

def test_macd_strategy():
    data = pd.DataFrame({'Close': [100, 102, 104, 103, 101]})
    results = macd_strategy(data)
    assert 'Signal' in results.columns
