import pandas as pd
from strategy import generate_signals
from backtest import backtest_strategy
from itertools import product


def optimize_parameters(data, ema_short_range, ema_long_range, rsi_range, rsi_oversold_range, rsi_overbought_range):
    """
    Perform optimization by testing different parameter combinations.

    :param data: DataFrame with OHLCV data.
    :param ema_short_range: Range of short EMA periods.
    :param ema_long_range: Range of long EMA periods.
    :param rsi_range: Range of RSI periods.
    :param rsi_oversold_range: Range of RSI oversold thresholds.
    :param rsi_overbought_range: Range of RSI overbought thresholds.
    :return: DataFrame with the results of optimization.
    """
    results = []

    # Iterate over all combinations of parameters
    for short_ema, long_ema, rsi_period, rsi_oversold, rsi_overbought in product(ema_short_range, ema_long_range, rsi_range, rsi_oversold_range, rsi_overbought_range):
        if short_ema >= long_ema:
            continue  # Skip invalid parameter combinations
        
        # Generate trading signals
        signals = generate_signals(data.copy(), short_ema, long_ema, rsi_period, rsi_overbought, rsi_oversold)
        
        # Backtest the strategy
        final_value, _ = backtest_strategy(signals)
        
        # Store the results
        results.append({
            'Short EMA': short_ema,
            'Long EMA': long_ema,
            'RSI Period': rsi_period,
            'RSI Oversold': rsi_oversold,
            'RSI Overbought': rsi_overbought,
            'Final Portfolio Value': final_value
        })
    
    # Convert results to DataFrame
    results_df = pd.DataFrame(results)
    return results_df

def get_best_parameters(results_df):
    """
    Get the parameter combination that produced the highest portfolio value.

    :param results_df: DataFrame with optimization results.
    :return: A row from the DataFrame with the best parameters.
    """
    best_params = results_df.loc[results_df['Final Portfolio Value'].idxmax()]
    return best_params


