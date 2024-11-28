import pandas as pd

def calculate_ema(series, period):
    """
    Calculate the Exponential Moving Average (EMA) of a given data series.
    
    :param series: Pandas Series containing the data (e.g., closing prices).
    :param period: The number of periods for the EMA calculation.
    :return: Pandas Series containing the EMA values.
    """
    return series.ewm(span=period, adjust=False).mean()

def calculate_rsi(series, period=14):
    """
    Calculate the Relative Strength Index (RSI) of a given data series.
    
    :param series: Pandas Series containing the data (e.g., closing prices).
    :param period: The number of periods for the RSI calculation.
    :return: Pandas Series containing the RSI values.
    """
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()

    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi
