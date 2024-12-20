# src/fetch_data.py

import pandas as pd
from binance.client import Client
from concurrent.futures import ThreadPoolExecutor
import os
import time

# Initialize the Binance client
client = Client(api_key='YOUR_API_KEY', api_secret='YOUR_API_SECRET')

def fetch_ohlcv(symbol, interval, start_str, end_str=None):
    """
    Fetch historical OHLCV data for a given symbol and interval.
    """
    klines = client.get_historical_klines(symbol, interval, start_str, end_str)
    data = pd.DataFrame(klines, columns=[
        'timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time',
        'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume',
        'taker_buy_quote_asset_volume', 'ignore'
    ])
    data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')
    data.set_index('timestamp', inplace=True)
    data = data[['open', 'high', 'low', 'close', 'volume']]
    data = data.astype(float)
    return data

def fetch_multiple_assets(pairs, interval, start_str, end_str=None):
    results = {}

    def fetch(pair):
        try:
            results[pair] = fetch_ohlcv(pair, interval, start_str, end_str)
        except Exception as e:
            print(f"Error fetching data for {pair}: {e}")

    with ThreadPoolExecutor() as executor:
        executor.map(fetch, pairs)

    return results
