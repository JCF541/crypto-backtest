import pandas as pd
from indicators import calculate_ema, calculate_rsi, calculate_macd, calculate_bollinger_bands, calculate_atr

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

def bollinger_band_strategy(data, period=20, std_dev=2):
    """
    Generate signals based on Bollinger Bands.
    Buy when price crosses below the lower band.
    Sell when price crosses above the upper band.
    :param data: DataFrame with 'Close' prices.
    :param period: Period for Bollinger Bands.
    :param std_dev: Standard deviation for bands.
    :return: DataFrame with 'Signal' column.
    """
    bb = calculate_bollinger_bands(data['Close'], period, std_dev)
    data = data.join(bb)
    data['Signal'] = 0
    data.loc[data['Close'] < data['Lower Band'], 'Signal'] = 1  # Buy
    data.loc[data['Close'] > data['Upper Band'], 'Signal'] = -1  # Sell
    return data

def macd_strategy(data, short_period=12, long_period=26, signal_period=9):
    """
    Generate signals based on MACD crossover.
    Buy when MACD crosses above Signal Line.
    Sell when MACD crosses below Signal Line.
    :param data: DataFrame with 'Close' prices.
    :param short_period: Short period for MACD.
    :param long_period: Long period for MACD.
    :param signal_period: Signal line period.
    :return: DataFrame with 'Signal' column.
    """
    macd = calculate_macd(data['Close'], short_period, long_period, signal_period)
    data = data.join(macd)
    data['Signal'] = 0
    data.loc[data['MACD'] > data['Signal Line'], 'Signal'] = 1  # Buy
    data.loc[data['MACD'] < data['Signal Line'], 'Signal'] = -1  # Sell
    return data

def atr_breakout_strategy(data, period=14, breakout_multiplier=2):
    atr = calculate_atr(data, period)
    data['Upper Breakout'] = data['Close'] + (breakout_multiplier * atr)
    data['Lower Breakout'] = data['Close'] - (breakout_multiplier * atr)
    data['Signal'] = 0
    data.loc[data['Close'] > data['Upper Breakout'], 'Signal'] = 1  # Buy
    data.loc[data['Close'] < data['Lower Breakout'], 'Signal'] = -1  # Sell
    return data
