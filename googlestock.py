import datetime
import pandas_datareader.data as web

start = datetime.datetime(2017, 1, 1)
end = datetime.datetime(2017, 8, 31)
f  = web.DataReader("aapl", 'google', start, end)
print(f)