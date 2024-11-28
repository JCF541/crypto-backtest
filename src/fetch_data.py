import os
from dotenv import load_dotenv
from binance.client import Client
from binance.exceptions import BinanceAPIException
import pandas as pd

# Load environment variables for API keys
load_dotenv()

API_KEY = os.getenv('BINANCE_API_KEY')
API_SECRET = os.getenv('BINANCE_API_SECRET')

# Initialize Binance client
client = Client(api_key=API_KEY, api_secret=API_SECRET)


def fetch_ohlcv(symbol, interval, start_str, end_str=None, save_to_csv=False, file_path=None):
    """
    Fetch historical OHLCV data from Binance in batches to handle API limits.

    :param symbol: Trading pair symbol (e.g., 'BTCUSDT').
    :param interval: Candlestick interval (e.g., '1h', '1d').
    :param start_str: Start date string in 'YYYY-MM-DD' format.
    :param end_str: End date string in 'YYYY-MM-DD' format (optional).
    :param save_to_csv: Whether to save the data to a CSV file (default: False).
    :param file_path: Path to save the CSV file (required if save_to_csv is True).
    :return: DataFrame with OHLCV data.
    """
    try:
        df_list = []
        while True:
            klines = client.get_historical_klines(
                symbol, interval, start_str, end_str, limit=1000
            )
            if not klines:
                break
            df = pd.DataFrame(klines, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume',
                                               'close_time', 'quote_asset_volume', 'number_of_trades',
                                               'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'])
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            df.set_index('timestamp', inplace=True)
            df = df[['open', 'high', 'low', 'close', 'volume']].astype(float)
            df_list.append(df)
            # Update start_str to the next batch's start time
            start_str = str(int(df.index[-1].timestamp() * 1000) + 1)
        
        result_df = pd.concat(df_list)

        if save_to_csv and file_path:
            result_df.to_csv(file_path)
            print(f"Data saved to {file_path}")

        return result_df
    except BinanceAPIException as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()
