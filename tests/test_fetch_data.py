import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.fetch_data import fetch_ohlcv

def test_fetch_ohlcv_valid_request():
    """Test fetching data with valid parameters."""
    df = fetch_ohlcv('BTCUSDT', '1h', '2023-01-01', '2023-01-02')
    assert not df.empty, "The DataFrame should not be empty."
    assert 'open' in df.columns, "DataFrame should have 'open' column."

def test_fetch_ohlcv_invalid_symbol():
    """Test fetching data with an invalid symbol."""
    df = fetch_ohlcv('INVALID', '1h', '2023-01-01', '2023-01-02')
    assert df.empty, "The DataFrame should be empty for an invalid symbol."
