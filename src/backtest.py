def backtest_strategy(data, initial_balance=1000, trading_fee=0.001):
    """
    Backtest a trading strategy based on generated signals.

    :param data: DataFrame containing OHLCV data and trading signals.
    :param initial_balance: Starting balance in USD.
    :param trading_fee: Trading fee per transaction.
    :return: Final portfolio value and DataFrame with backtest results.
    """
    balance = initial_balance
    btc_balance = 0
    portfolio_value = []

    for i in range(len(data)):
        row = data.iloc[i]
        
        # Execute buy signal
        if row['signal'] == 1 and balance > 0:
            btc_balance = (balance * (1 - trading_fee)) / row['close']
            balance = 0

        # Execute sell signal
        elif row['signal'] == -1 and btc_balance > 0:
            balance = btc_balance * row['close'] * (1 - trading_fee)
            btc_balance = 0

        # Calculate portfolio value
        portfolio_value.append(balance + btc_balance * row['close'])

    # Add portfolio value to DataFrame
    data['portfolio_value'] = portfolio_value
    return data['portfolio_value'].iloc[-1], data
