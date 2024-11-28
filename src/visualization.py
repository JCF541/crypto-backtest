import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def visualize_optimization_results(results_df):
    """
    Visualize the optimization results using a heatmap.

    :param results_df: DataFrame with optimization results.
    """
    pivot = results_df.pivot_table(index='RSI Period', columns='RSI Overbought', values='Final Portfolio Value')
    plt.figure(figsize=(10, 7))
    plt.title("Optimization Results: Final Portfolio Value")
    plt.imshow(pivot, cmap='viridis', aspect='auto', interpolation='nearest')
    plt.colorbar(label='Final Portfolio Value')
    plt.xlabel('RSI Overbought')
    plt.ylabel('RSI Period')
    plt.xticks(ticks=range(len(pivot.columns)), labels=pivot.columns)
    plt.yticks(ticks=range(len(pivot.index)), labels=pivot.index)
    plt.show()

def plot_portfolio_performance(portfolio_log):
    """
    Plot the performance of the portfolio over time.
    """
    portfolio_log['cumulative_profit'] = portfolio_log['profit'].cumsum()
    plt.figure(figsize=(10, 6))
    plt.plot(portfolio_log['pair'], portfolio_log['cumulative_profit'], marker='o')
    plt.title('Portfolio Cumulative Profit Over Time')
    plt.xlabel('Asset Pair')
    plt.ylabel('Cumulative Profit')
    plt.grid(True)
    plt.show()


def save_optimization_heatmap(results_df, save_to_file=None):
    """
    Save a heatmap visualization of optimization results.

    :param results_df: DataFrame with optimization results.
    :param save_to_file: File path to save the heatmap (optional).
    """
    pivot = results_df.pivot_table(index='RSI Period', columns='RSI Overbought', values='Final Portfolio Value')
    plt.figure(figsize=(10, 7))
    plt.title("Optimization Results: Final Portfolio Value")
    plt.imshow(pivot, cmap='viridis', aspect='auto', interpolation='nearest')
    plt.colorbar(label='Final Portfolio Value')
    plt.xlabel('RSI Overbought')
    plt.ylabel('RSI Period')
    plt.xticks(ticks=range(len(pivot.columns)), labels=pivot.columns)
    plt.yticks(ticks=range(len(pivot.index)), labels=pivot.index)

    if save_to_file:
        plt.savefig(save_to_file)
        print(f"Optimization heatmap saved to {save_to_file}")

    plt.show()

def generate_report(data, results_df, portfolio_plot_path, heatmap_path, report_path):
    """
    Generate a comprehensive report with visualizations and optimization results.

    :param data: DataFrame with backtest results.
    :param results_df: DataFrame with optimization results.
    :param portfolio_plot_path: File path for portfolio performance plot.
    :param heatmap_path: File path for optimization heatmap.
    :param report_path: File path to save the report text.
    """
    # Save visualizations
    plot_portfolio_performance(data, save_to_file=portfolio_plot_path)
    save_optimization_heatmap(results_df, save_to_file=heatmap_path)

    # Write a textual summary
    with open(report_path, 'w') as f:
        f.write("=== Backtest Summary ===\n")
        f.write(f"Final Portfolio Value: {data['portfolio_value'].iloc[-1]:.2f}\n")
        f.write(f"Number of Trades: {len(data[data['signal'] != 0])}\n")
        f.write("\n=== Best Optimization Parameters ===\n")
        best_params = results_df.loc[results_df['Final Portfolio Value'].idxmax()]
        f.write(best_params.to_string())
    
    print(f"Report saved to {report_path}")

def plot_correlation_heatmap(pairs, interval, start_str, end_str):
    """
    Plot a heatmap of asset correlations.
    """
    data_dict = {}
    for pair in pairs:
        data = pd.read_csv(f"data/{pair}_{interval}.csv", index_col='timestamp', parse_dates=True)
        data_dict[pair] = data['close']

    df = pd.DataFrame(data_dict)
    correlation_matrix = df.corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Asset Correlation Heatmap')
    plt.show()