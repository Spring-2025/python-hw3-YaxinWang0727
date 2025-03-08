import yfinance as yf
import pandas as pd
import numpy as np

def YahooData2returns(YahooData):
    if 'Adj Close' not in YahooData.columns:
        raise ValueError("YahooData must contain 'Adj Close' column")
    
    pricevec = YahooData['Adj Close'].values
    if len(pricevec) < 2:
        raise ValueError("Not enough data points to calculate returns")
    
    n = len(pricevec)
    ratiovec = pricevec[1:n]/pricevec[:n-1]
    returns = ratiovec - 1
    return returns


def get_stock_data(symbol):
    data = yf.download(symbol)
    print(data)
    prices = data['Close']
    return prices

# Example usage
prices = get_stock_data('GS')
print(type(prices))
pricevec = prices.values


# Compute the returns
n = len(pricevec)
ratiovec = pricevec[1:n] / pricevec[:n-1]

def get_returns(pricevec):
    if len(pricevec) < 2:
        raise ValueError("Not enough data points to calculate returns")
    n = len(pricevec)
    ratiovec = pricevec[1:n] / pricevec[:n-1]
    returns = ratiovec - 1  # assuming the return calculation is (price_t / price_t-1) - 1
    return returns


# Example of using get_returns
returns = get_returns(pricevec)
print(returns)

# Steps
# Download data
# Extract 'Adj Close' column
# Extract values from 'Adj Close' column to transform to a simple array
# Calculate and return the lagged returns

#unit test
d = { 'Open': [100, 102, 101, 103],

'High': [105, 104, 103, 105],

'Low': [98, 100, 99, 101],

'Close': [101, 103, 102, 104],

'Adj Close': [101, 103, 102, 104],

'Volume': [1000, 1200, 900, 1100]}



index = pd.to_datetime(['2023-10-26', '2023-10-27', '2023-10-28', '2023-10-29'])

tempdata = pd.DataFrame(d, index=index)

returns = YahooData2returns(tempdata)

np.isclose(returns[0], 0.01980198, atol=0.01)

np.isclose(returns[1], -0.00970874, atol=0.01)

np.isclose(returns[2], 0.01960784, atol=0.01)

print("Unit test passed!")
