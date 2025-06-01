from textblob import TextBlob
import pandas as pd

def compute_sentiment(df: pd.DataFrame) -> pd.DataFrame:
    df['sentiment_score'] = df['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
    return df
