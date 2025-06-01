from src.data_loader import load_news_data
from src.eda import headline_stats, publisher_analysis, date_analysis
from src.sentiment import compute_sentiment

def run():
    path = "data/raw_analyst_ratings.csv"
    df = load_news_data(path)
    
    # Basic Text Analysis
    headline_stats(df)
    publisher_analysis(df)
    date_analysis(df)
    
    # Sentiment Analysis
    df = compute_sentiment(df)
    print(df[['headline', 'sentiment_score']].head())

if __name__ == "__main__":
    run()
