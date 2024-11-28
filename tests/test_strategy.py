import pytest
from src.strategy import generate_signals
import pandas as pd

def test_generate_signals():
    """Test trading signal generation."""
    data = pd.DataFrame({
        'close': [100, 105, 110, 115, 120, 125, 130, 135, 140, 145]
    })
    signals = generate_signals(data, short_ema_period=3, long_ema_period=5, rsi_period=2, rsi_overbought=80, rsi_oversold=20)
    assert 'signal' in signals.columns, "Signal column should be present in DataFrame."