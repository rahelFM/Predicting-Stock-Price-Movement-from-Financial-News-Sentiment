import pandas as pd

def compute_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute SMA, EMA, RSI, MACD using TA-Lib.
    Applies per stock if multiple stocks are present.
    """
    results = []
    for stock in df['Stock'].unique():
        stock_df = df[df['Stock'] == stock].copy()
        
        # Convert Close column to float
        close = stock_df['Close'].astype(float).values

        stock_df['SMA_20'] = talib.SMA(close, timeperiod=20)
        stock_df['EMA_20'] = talib.EMA(close, timeperiod=20)
        stock_df['RSI_14'] = talib.RSI(close, timeperiod=14)
        macd, macdsignal, _ = talib.MACD(close, fastperiod=12, slowperiod=26, signalperiod=9)
        stock_df['MACD'] = macd
        stock_df['MACD_Signal'] = macdsignal

        results.append(stock_df)
    
    return pd.concat(results).reset_index(drop=True)
