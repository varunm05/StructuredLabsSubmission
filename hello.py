import pandas as pd
import plotly.express as px
import preswald
import plotly.graph_objects as go

preswald.connect()
preswald.text("# Apple and Google Stock Comparison")

preswald.text("The complete dataset, spanning from 2010 to 2024, including data for Nvidia, Amazon, and and Microsoft")
df = preswald.get_df('data/stockdata.csv')

preswald.table(df.head(10))
aaplDf = df[["Date", "Close_AAPL", "High_AAPL", "Low_AAPL", "Open_AAPL"]]
aapl2023 = aaplDf.tail(500)

preswald.text("Candlestick chart for AAPL, from 2023 to end of 2024:")
aapl2023Graph = go.Figure(data=[go.Candlestick(x=aapl2023['Date'],
                open=aapl2023['Open_AAPL'],
                high=aapl2023['High_AAPL'],
                low=aapl2023['Low_AAPL'],
                close=aapl2023['Close_AAPL'])])

preswald.plotly(aapl2023Graph)

googlDf = df[['Date', 'Close_GOOGL', 'High_GOOGL', 'Low_GOOGL', 'Open_GOOGL']]
googl2023 = googlDf.tail(500)

preswald.text("Candlestick chart for GOOGL, from 2023 to end of 2024:")
googl2023Graph = go.Figure(data=[go.Candlestick(x=googl2023['Date'],
                open=googl2023['Open_GOOGL'],
                high=googl2023['High_GOOGL'],
                low=googl2023['Low_GOOGL'],
                close=googl2023['Close_GOOGL'])])

preswald.plotly(googl2023Graph)

