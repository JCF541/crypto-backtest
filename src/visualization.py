import matplotlib.pyplot as plt
import pandas as pd

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

def plot_portfolio_performance(data, save_to_file=None):
    """
    Plot portfolio value over time with trade signals.

    :param data: DataFrame with 'portfolio_value' and 'close' columns.
    :param save_to_file: File path to save the plot (optional).
    """
    plt.figure(figsize=(14, 7))
    plt.plot(data.index, data['portfolio_value'], label='Portfolio Value', color='blue')
    plt.plot(data.index, data['close'], label='Price', color='gray', alpha=0.5)
    
    # Plot buy signals
    buy_signals = data[data['signal'] == 1]
    plt.scatter(buy_signals.index, buy_signals['close'], label='Buy Signal', marker='^', color='green')
    
    # Plot sell signals
    sell_signals = data[data['signal'] == -1]
    plt.scatter(sell_signals.index, sell_signals['close'], label='Sell Signal', marker='v', color='red')
    
    plt.title("Portfolio Performance")
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.legend()
    plt.grid()

    if save_to_file:
        plt.savefig(save_to_file)
        print(f"Portfolio performance plot saved to {save_to_file}")

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