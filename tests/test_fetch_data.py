import pytest
import sys
import os
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from fetch_data import fetch_multiple_assets, fetch_ohlcv

def test_fetch_ohlcv_valid_request():
    """Test fetching data with valid parameters."""
    df = fetch_ohlcv('BTCUSDT', '1h', '2023-01-01', '2023-01-02')
    assert not df.empty, "The DataFrame should not be empty."
    assert 'open' in df.columns, "DataFrame should have 'open' column."

def test_fetch_ohlcv_invalid_symbol():
    """Test fetching data with an invalid symbol."""
    df = fetch_ohlcv('INVALID', '1h', '2023-01-01', '2023-01-02')
    assert df.empty, "The DataFrame should be empty for an invalid symbol."

class TestFetchData(unittest.TestCase):

    def test_fetch_multiple_assets(self):
        pairs = ['BTCUSDT', 'ETHUSDT']
        interval = '1h'
        start_str = '1 Jan, 2021'
        end_str = '1 Feb, 2021'
        data_dict = fetch_multiple_assets(pairs, interval, start_str, end_str)
        self.assertEqual(len(data_dict), len(pairs))
        for pair in pairs:
            self.assertIn(pair, data_dict)
            self.assertFalse(data_dict[pair].empty)