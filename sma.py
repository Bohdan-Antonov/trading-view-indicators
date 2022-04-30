# Simple Moving Average


def moving_average(close_price, period):
    sma_values = []
    for i in range(len(close_price)):
        sma_values.append((sum(close_price[i:i + period])) / period)
    return sma_values[:-period+1]