# Stock Market Data Visualizer

**Author:** Charles Eleri

## Overview

This is a Python-based **Stock Market Data Visualizer** that fetches real-time stock data from the **Alpha Vantage API**, processes it using **Pandas**, and displays an interactive graph with **Matplotlib**. This version is designed for **command-line execution**, removing the dependency on a GUI (Tkinter).

## Features

- Fetch stock market data from Alpha Vantage API
- Visualize closing prices over time using Matplotlib
- Simple command-line interface for easy stock symbol input
- Data processing with Pandas for better insights

## Installation

### **Prerequisites**

Ensure you have Python installed (>=3.7). Then, install the required dependencies:

```sh
pip install requests pandas matplotlib
```

## How to Use

1. **Get an API Key** from [Alpha Vantage](https://www.alphavantage.co/support/#api-key).
2. **Insert your API Key** into the script (already pre-configured):
   ```python
   API_KEY = "21YYWNHZ2DFIUIPX"  # Replace with your Alpha Vantage API Key if needed
   ```
3. **Run the script** in the command line:
   ```sh
   python stock_visualizer.py
   ```
4. **Enter a stock symbol** (e.g., `AAPL`, `GOOGL`) when prompted.
5. **View the stock price trend** in the generated chart.

## Example Output

- The program prompts you to enter a stock symbol.
- The script fetches and processes the stock data.
- A Matplotlib chart displays the stock's closing price trend.

## API Key Insertion

To use this tool with your personal **Alpha Vantage API Key**, update this section in `fetch_stock_data()`:

```python
API_KEY = "your_actual_api_key_here"  # Replace with your Alpha Vantage API Key
```

## Future Enhancements

- Add support for multiple stock symbols in one chart
- Implement moving average indicators
- Save fetched data as CSV for further analysis

## License


Developed by Charles Eleri - Building financial analytics.


API key
API_KEY = "your_actual_api_key_here"  # Replace with your Alpha
