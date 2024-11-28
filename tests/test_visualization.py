import unittest
import pandas as pd
from visualization import plot_portfolio_performance

class TestVisualization(unittest.TestCase):

    def test_plot_portfolio_performance(self):
        data = pd.DataFrame({
            'close': [100, 110, 120, 115, 125],
            'portfolio_value': [1000, 1100, 1200, 1150, 1250],
            'signal': [0, 1, 0, -1, 0],
            'profit': [0, 100, 200, -50, 100]  # Added profit column
        })

        try:
            plot_portfolio_performance(data)  # Should run without exceptions
        except Exception as e:
            self.fail(f"plot_portfolio_performance raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
