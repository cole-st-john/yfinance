"""File to demonstrate some current issues around period='max'"""

import yfinance as yf

INTRADAY_INTERVALS = ["1m", "2m", "5m", "15m", "30m", "60m", "1h", "90m"]
DAY_PLUS_INTERVALS = ["1d", "5d", "1wk", "1mo", "3mo"]
INTERVALS = [*INTRADAY_INTERVALS, *DAY_PLUS_INTERVALS]
TICKERS = ["EURUSD=X"]

for interval in INTERVALS:
    df = yf.download(tickers=TICKERS, period="max", interval=interval, progress=False, auto_adjust=True)
    print(f"- failed for {interval}!!!") if df.empty else print(f"- passed for {interval}")
