import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def headline_stats(df: pd.DataFrame):
    df['headline_length'] = df['headline'].str.len()
    print(df['headline_length'].describe())

def publisher_analysis(df: pd.DataFrame):
    publisher_counts = df['publisher'].value_counts()
    print(publisher_counts.head())
    publisher_counts.head(10).plot(kind='bar', title="Top 10 Publishers")
    plt.tight_layout()
    plt.show()

def date_analysis(df: pd.DataFrame):
    df['publish_day'] = df['date'].dt.date
    daily_counts = df.groupby('publish_day').size()
    daily_counts.plot(figsize=(12,6), title="Daily Article Volume")
    plt.tight_layout()
    plt.show()


  
data_path = "data/raw_analyst_ratings.csv"  

df = pd.read_csv(data_path)  # then use it

    # Load the dataset
df = pd.read_csv(data_path, parse_dates=['date'])
    
print("Running Headline Length Stats:")
headline_stats(df)
    
print("\nRunning Publisher Analysis:")
publisher_analysis(df)
    
print("\nRunning Date Analysis:")
date_analysis(df)
