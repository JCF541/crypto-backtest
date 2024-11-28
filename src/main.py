from fetch_data import fetch_ohlcv
from strategy import generate_signals
from backtest import backtest_strategy
from optimization import optimize_parameters
from visualization import generate_report

if __name__ == "__main__":
    # Fetch data
    data = fetch_ohlcv("BTCUSDT", "1h", "2023-01-01", "2023-01-15")

    # Generate signals and backtest
    signals = generate_signals(data)
    final_value, backtest_results = backtest_strategy(signals)

    # Optimize parameters
    results_df = optimize_parameters(
        data,
        ema_short_range=range(10, 20, 2),
        ema_long_range=range(20, 40, 5),
        rsi_range=range(10, 20, 5),
        rsi_oversold_range=range(20, 40, 5),
        rsi_overbought_range=range(60, 80, 5)
    )

    # Generate visualizations and report
    generate_report(
        backtest_results,
        results_df,
        portfolio_plot_path="data/results/portfolio_performance.png",
        heatmap_path="data/results/optimization_heatmap.png",
        report_path="data/results/report.txt"
    )
