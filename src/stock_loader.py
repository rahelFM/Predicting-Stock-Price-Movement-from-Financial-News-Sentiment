import os
import pandas as pd

def load_stock_data_from_folder(folder_path=None):
    """
    Load all stock CSV files from a folder and combine them into a single DataFrame.
    """
    if folder_path is None:
    
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        folder_path = os.path.join(base_dir, "data", "yfinance_data")

    stock_data = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            symbol = filename.split("_")[0]
            file_path = os.path.join(folder_path, filename)
            df = pd.read_csv(file_path)
            df["Symbol"] = symbol
            stock_data.append(df)

    if stock_data:
        return pd.concat(stock_data, ignore_index=True)
    else:
        print("⚠️ No CSV files found in the folder.")
        return pd.DataFrame()

if __name__ == "__main__":
    df = load_stock_data_from_folder()
    print(df.head())
