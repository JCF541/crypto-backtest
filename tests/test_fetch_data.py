import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from fetch_data import fetch_ohlcv, fetch_multiple_assets
from binance.exceptions import BinanceAPIException

class TestFetchData(unittest.TestCase):

    def test_fetch_ohlcv_invalid_symbol(self):
        with self.assertRaises(BinanceAPIException):
            fetch_ohlcv('INVALID', '1h', '2023-01-01', '2023-01-02')

    def test_fetch_multiple_assets(self):
        pairs = ['BTCUSDT', 'ETHUSDT']
        interval = '1h'
        start_str = '1 Jan, 2021'
        end_str = '1 Feb, 2021'

        data_dict = fetch_multiple_assets(pairs, interval, start_str, end_str)
        self.assertEqual(len(data_dict), len(pairs), "Data should be fetched for all pairs")
        for pair in pairs:
            self.assertIn(pair, data_dict)
            self.assertFalse(data_dict[pair].empty)

if __name__ == '__main__':
    unittest.main()
