import unittest
import pandas as pd
from optimization import optimize_parameters

class TestOptimization(unittest.TestCase):

    def test_optimize_parameters(self):
        data = pd.DataFrame({
            'close': [100, 110, 105, 120, 115]
        })

        ema_short_range = range(5, 10, 5)
        ema_long_range = range(10, 15, 5)
        rsi_range = range(10, 20, 10)
        rsi_oversold_range = range(20, 30, 10)
        rsi_overbought_range = range(70, 80, 10)

        results_df = optimize_parameters(
            data,
            ema_short_range,
            ema_long_range,
            rsi_range,
            rsi_oversold_range,
            rsi_overbought_range
        )

        self.assertFalse(results_df.empty, "Optimization results should not be empty")
        self.assertIn('Final Portfolio Value', results_df.columns, "Results should include final portfolio value")

if __name__ == '__main__':
    unittest.main()
