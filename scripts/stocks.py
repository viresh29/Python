import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

# https://medium.com/@patrick.collins_58673/stock-api-landscape-5c6e054ee631

api_key = '4A57ZR3CD48VDU0Q'

ts = TimeSeries(key=api_key, output_format='pandas')

data, meta_data = ts.get_intraday(
    symbol='AAPL', interval='60min', outputsize='full')

print(data)
