from binance.client import Client
from binance.exceptions import BinanceAPIException
import pandas as pd

def fetch_ohlcv(symbol, interval, start_str, end_str=None):
    """
    Fetch historical OHLCV data from Binance.

    :param symbol: Trading pair symbol (e.g., 'BTCUSDT')
    :param interval: Candlestick interval (e.g., '1h', '1d')
    :param start_str: Start date string in 'YYYY-MM-DD'
    :param end_str: End date string in 'YYYY-MM-DD' (optional)
    :return: DataFrame with OHLCV data
    """
    client = Client(api_key='your_api_key', api_secret='your_api_secret')  # Replace with your API keys

    try:
        klines = client.get_historical_klines(symbol, interval, start_str, end_str)
        df = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume',
                                           'close_time', 'quote_asset_volume', 'number_of_trades',
                                           'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.set_index('timestamp', inplace=True)
        df = df[['open', 'high', 'low', 'close', 'volume']].astype(float)
        return df
    except BinanceAPIException as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()
