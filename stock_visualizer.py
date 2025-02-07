import requests
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

# Function to fetch stock data from Alpha Vantage API
def fetch_stock_data(symbol):
    API_KEY = "demo"  # Replace with actual API key
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}&outputsize=compact"
    response = requests.get(url)
    data = response.json()
    time_series = data.get("Time Series (Daily)", {})
    
    # Convert to DataFrame
    df = pd.DataFrame.from_dict(time_series, orient='index')
    df = df.astype(float)
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    df.rename(columns={"1. open": "Open", "2. high": "High", "3. low": "Low", "4. close": "Close", "5. volume": "Volume"}, inplace=True)
    
    return df

# Function to plot stock data
def plot_stock_data(df, symbol):
    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df['Close'], marker='o', linestyle='-', label=f'{symbol} Closing Price')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.title(f'{symbol} Stock Price Over Time')
    plt.legend()
    plt.grid()
    plt.show()

# GUI Application
def main():
    def on_search():
        symbol = symbol_entry.get().upper()
        df = fetch_stock_data(symbol)
        if not df.empty:
            plot_stock_data(df, symbol)
        else:
            result_label.config(text="Error fetching data. Try again.")

    root = tk.Tk()
    root.title("Stock Market Data Visualizer")
    root.geometry("400x200")
    
    ttk.Label(root, text="Enter Stock Symbol:").pack(pady=5)
    symbol_entry = ttk.Entry(root)
    symbol_entry.pack(pady=5)
    
    search_button = ttk.Button(root, text="Fetch & Plot Data", command=on_search)
    search_button.pack(pady=10)
    
    result_label = ttk.Label(root, text="")
    result_label.pack()
    
    root.mainloop()

if __name__ == "__main__":
    main()
