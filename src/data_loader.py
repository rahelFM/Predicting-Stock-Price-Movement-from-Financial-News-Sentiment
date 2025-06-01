import pandas as pd

def load_news_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["date"])
    df['date'] = pd.to_datetime(df['date'], utc=True)
    return df
