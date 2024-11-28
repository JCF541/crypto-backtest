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

def calculate_bollinger_bands(data, period=20, std_dev=2):
    """
    Calculate Bollinger Bands.
    :param data: Series of prices.
    :param period: Number of periods for SMA.
    :param std_dev: Number of standard deviations for the bands.
    :return: DataFrame with 'SMA', 'Upper Band', and 'Lower Band'.
    """
    sma = data.rolling(window=period).mean()
    std = data.rolling(window=period).std()
    upper_band = sma + (std_dev * std)
    lower_band = sma - (std_dev * std)
    return pd.DataFrame({'SMA': sma, 'Upper Band': upper_band, 'Lower Band': lower_band})

def calculate_macd(data, short_period=12, long_period=26, signal_period=9):
    """
    Calculate MACD and Signal Line.
    :param data: Series of prices.
    :param short_period: Period for the short EMA.
    :param long_period: Period for the long EMA.
    :param signal_period: Period for the signal line EMA.
    :return: DataFrame with 'MACD' and 'Signal Line'.
    """
    short_ema = data.ewm(span=short_period, adjust=False).mean()
    long_ema = data.ewm(span=long_period, adjust=False).mean()
    macd = short_ema - long_ema
    signal_line = macd.ewm(span=signal_period, adjust=False).mean()
    return pd.DataFrame({'MACD': macd, 'Signal Line': signal_line})

def calculate_atr(data, period=14):
    """
    Calculate Average True Range (ATR).
    :param data: DataFrame with 'High', 'Low', and 'Close' prices.
    :param period: Number of periods for ATR.
    :return: Series of ATR values.
    """
    high_low = data['High'] - data['Low']
    high_close = (data['High'] - data['Close'].shift()).abs()
    low_close = (data['Low'] - data['Close'].shift()).abs()
    true_range = high_low.combine(high_close, max).combine(low_close, max)
    atr = true_range.rolling(window=period).mean()
    return atr



