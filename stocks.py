import yfinance as yf
import streamlit as slt
import pandas as pd

slt.write("""
# Simple Stock Price app
Shown are the stock **closing price** and **volume** of google
""")

#define the ticker symbol
tickerSymbol = 'GOOGL'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d',start="2015-9-2", end='2020-9-2')

#open High low Close Volume Dividends Stock Splits
slt.write("""
## Closing price##
""")
slt.line_chart(tickerDf.Close)
slt.write("""
## Volume price##
""")
slt.line_chart(tickerDf.Volume)
