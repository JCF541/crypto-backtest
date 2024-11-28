# src/backtest.py

import pandas as pd
from strategy import apply_strategy
from indicators import calculate_indicators  # Ensure this import is correct

def backtest_strategy(data, strategy_function, initial_balance=1000, trading_fee=0.001, position_size=0.1):
    """
    Backtest a given strategy on historical data.
    """
    balance = initial_balance
    positions = []
    trade_log = []

    data = calculate_indicators(data)
    data = strategy_function(data)

    for index, row in data.iterrows():
        if row['Signal'] == 1 and balance > 0:
            # Buy
            amount = balance * position_size
            balance -= amount
            positions.append({'entry_price': row['close'], 'amount': amount, 'entry_time': index})
            trade_log.append({'time': index, 'type': 'buy', 'price': row['close'], 'amount': amount})
        elif row['Signal'] == -1 and positions:
            # Sell
            position = positions.pop(0)
            profit = (row['close'] - position['entry_price']) * (position['amount'] / position['entry_price'])
            balance += position['amount'] + profit
            trade_log.append({'time': index, 'type': 'sell', 'price': row['close'], 'amount': position['amount'], 'profit': profit})

    return balance, pd.DataFrame(trade_log)

def portfolio_backtest(pairs, interval, start_str, end_str, strategy_function, initial_balance=1000, trading_fee=0.001, position_size=0.1):
    """
    Perform portfolio backtesting across multiple assets.
    """
    total_balance = initial_balance
    portfolio_log = []

    for pair in pairs:
        data = pd.read_csv(f"data/{pair}_{interval}.csv", index_col='timestamp', parse_dates=True)
        final_balance, trade_log = backtest_strategy(data, strategy_function, initial_balance=total_balance * position_size, trading_fee=trading_fee, position_size=position_size)
        profit = final_balance - (total_balance * position_size)
        total_balance += profit
        portfolio_log.append({'pair': pair, 'final_balance': final_balance, 'profit': profit})

    return total_balance, pd.DataFrame(portfolio_log)
