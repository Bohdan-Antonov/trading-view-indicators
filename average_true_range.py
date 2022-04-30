import pandas


# True Range


def true_range(high_price, low_price, close_price):
    x = high_price - low_price
    y = abs(high_price - close_price)
    z = abs(low_price - close_price)
    if y <= x >= z:
        tr = x
    elif x <= y >= z:
        tr = y
    elif x <= z >= y:
        tr = z
    return tr


# Average True Range


def average_true_range(low_price, close_price, period):
    x = 1
    true_ranges = []
    while x < len(close_price):
        tr = true_range(close_price[x], low_price[x], close_price[x-1])
        true_ranges.append(tr)
        x += 1
    true_ranges = pandas.DataFrame(true_ranges)
    atr_df = true_ranges.ewm(com=(period - 1), min_periods=period).mean()
    atr_values = []
    for i in atr_df.dropna().values.tolist():
        atr_values.append(i[0])
    return atr_values
