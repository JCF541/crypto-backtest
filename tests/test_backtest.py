import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
import unittest
import pandas as pd
from backtest import portfolio_backtest
from strategy import macd_strategy

class TestBacktest(unittest.TestCase):

    def setUp(self):
        # Create sample data for two assets
        self.data_btc = pd.DataFrame({
            'timestamp': pd.date_range('2023-01-01', periods=5, freq='D'),
            'open': [100, 102, 104, 106, 108],
            'high': [110, 112, 114, 116, 118],
            'low': [90, 92, 94, 96, 98],
            'close': [105, 103, 107, 109, 111],
            'volume': [1000, 1100, 1200, 1300, 1400]
        }).set_index('timestamp')

        self.data_eth = pd.DataFrame({
            'timestamp': pd.date_range('2023-01-01', periods=5, freq='D'),
            'open': [50, 51, 52, 53, 54],
            'high': [55, 56, 57, 58, 59],
            'low': [45, 46, 47, 48, 49],
            'close': [52, 53, 54, 55, 56],
            'volume': [500, 600, 700, 800, 900]
        }).set_index('timestamp')

        self.data_dict = {
            'BTCUSDT': self.data_btc,
            'ETHUSDT': self.data_eth
        }

    def test_portfolio_backtest(self):
        """
        Test portfolio backtesting with two assets.
        """
        final_balance, portfolio_log = portfolio_backtest(
            self.data_dict,
            macd_strategy,
            initial_balance=1000,
            trading_fee=0.001,
            position_size=0.5
        )

        self.assertGreater(final_balance, 0, "Final balance should be greater than 0.")
        self.assertFalse(portfolio_log.empty, "Portfolio log should not be empty.")
        self.assertIn('pair', portfolio_log.columns, "Portfolio log should include 'pair' column.")
        self.assertIn('profit', portfolio_log.columns, "Portfolio log should include 'profit' column.")

if __name__ == '__main__':
    unittest.main()
