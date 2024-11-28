import pandas as pd
from src.indicators import calculate_ema, calculate_rsi

def generate_signals(data, short_ema_period=12, long_ema_period=26, rsi_period=14, rsi_overbought=70, rsi_oversold=30):
    """
    Generate trading signals based on EMA crossover and RSI levels.

    :param data: DataFrame containing OHLCV data.
    :param short_ema_period: Period for short EMA.
    :param long_ema_period: Period for long EMA.
    :param rsi_period: Period for RSI.
    :param rsi_overbought: RSI overbought threshold.
    :param rsi_oversold: RSI oversold threshold.
    :return: DataFrame with trading signals.
    """
    # Calculate indicators
    data['short_ema'] = calculate_ema(data['close'], short_ema_period)
    data['long_ema'] = calculate_ema(data['close'], long_ema_period)
    data['rsi'] = calculate_rsi(data['close'], rsi_period)

    # Initialize signals column
    data['signal'] = 0

    # Buy signal: Short EMA crosses above Long EMA, RSI < Oversold
    data.loc[(data['short_ema'] > data['long_ema']) & (data['rsi'] < rsi_oversold), 'signal'] = 1

    # Sell signal: Short EMA crosses below Long EMA, RSI > Overbought
    data.loc[(data['short_ema'] < data['long_ema']) & (data['rsi'] > rsi_overbought), 'signal'] = -1

    return data
