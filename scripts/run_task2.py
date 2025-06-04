import os
import matplotlib.pyplot as plt
from src.stock_loader import load_stock_data
from src.technical_indicators import compute_indicators

DATA_PATH = 'data/stock_prices.csv'   # Replace with your actual file
OUTPUT_DIR = 'output/task2_charts'
os.makedirs(OUTPUT_DIR, exist_ok=True)

def plot_indicators(df):
    for stock in df['Stock'].unique():
        stock_df = df[df['Stock'] == stock]
        plt.figure(figsize=(12, 6))
        plt.plot(stock_df['Date'], stock_df['Close'], label='Close')
        plt.plot(stock_df['Date'], stock_df['SMA_20'], label='SMA 20')
        plt.plot(stock_df['Date'], stock_df['EMA_20'], label='EMA 20')
        plt.title(f'{stock} Price & Moving Averages')
        plt.legend()
        plt.savefig(f'{OUTPUT_DIR}/{stock}_sma_ema.png')
        plt.close()

if __name__ == '__main__':
    df = load_stock_data(DATA_PATH)
    df = compute_indicators(df)
    df.to_csv('output/enriched_stock_data.csv', index=False)
    plot_indicators(df)
    print("✅ Task 2 complete: indicators calculated and plots saved.")
