import math
import pandas


# Simple Moving Average


def moving_average(close_price, period):
    sma_values = []
    for i in range(len(close_price)):
        sma_values.append((sum(close_price[i:i + period])) / period)
    return sma_values[:-period+1]


# Exponential Moving Average


def exponential_moving_average(close_price, period):
    sma_list = moving_average(close_price, period)
    multiplier = 2 / float(period + 1)
    ema_values = []
    ema_start = (((close_price[period + 1] - sma_list[0]) * multiplier) + sma_list[0])
    ema_values.append(ema_start)
    for i in range(len(close_price[period:]) - 2):
        ema_values.append((close_price[i + period + 2] - ema_values[i]) * multiplier + ema_values[i])
    return ema_values


# Moving Average Convergence Divergence


def macd(close_price, fast=12, slow=26):
    ema_slow = exponential_moving_average(close_price, slow)
    ema_fast = exponential_moving_average(close_price, fast)[-len(ema_slow):]
    macd_line = []
    for i in range(len(ema_slow)):
        macd_line.append(ema_fast[i] - ema_slow[i])
    signal_line = exponential_moving_average(macd_line, 9)
    macd_line = macd_line[-len(signal_line):]
    histogram = []
    for i in range(len(signal_line)):
        histogram.append(macd_line[i] - signal_line[i])
    return macd_line, signal_line, histogram


# Relative Strength Index


def relative_strength_index(close_price, period):
    delta = close_price.diff()
    delta = delta[1:]
    up, down = delta.copy(), delta.copy()
    up[up < 0.0] = 0.0
    down[down > 0.0] = 0.0
    roll_up = up.ewm(com=(period - 1), min_periods=period).mean()
    roll_down = down.abs().ewm(com=(period - 1), min_periods=period).mean()
    rs = roll_up / roll_down
    rsi = 100.0 - (100.0 / (1.0 + rs))
    rsi_values = []
    for i in rsi:
        rsi_values.append(i)
    return rsi_values


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


# On Balance Volume


def on_balance_volume(close_price, volume):
    obv_values = []
    obv = 0
    for i in range(len(close_price)):
        if i == 0:
            obv_values.append(obv)
        else:
            if close_price[i] > close_price[i - 1]:
                obv += (volume[i] / 1000000)
            elif close_price[i] == close_price[i - 1]:
                pass
            elif close_price[i] < close_price[i - 1]:
                obv -= (volume[i] / 1000000)
            obv_values.append(round(obv, 3))
    return obv_values


# Elder's Force Index


def force_index(close_price, volume):
    force_index_values = []
    for i in range(len(close_price)):
        if i == 0:
            force_index_values.append(0)
        else:
            f_index = (volume[i] / 1000000) * (close_price[i] - close_price[i - 1])
            force_index_values.append(round(f_index, 3))
    return force_index_values


# Standard Deviation


def standard_deviation(close_price, period):
    std_dev_values = []
    for i in range(len(close_price) - (period - 1)):
        mean = sum(close_price[i:i + period]) / period
        dev = []
        dev_sq = []
        for x in close_price[i:i + period]:
            dev.append((x - mean))
            dev_sq.append(abs(pow((x - mean), 2)))
        std_dev = math.sqrt((sum(dev_sq) / period))
        std_dev_values.append(std_dev)
    return std_dev_values


# Bollinger Bands


def bollinger_bands(close_price, period):
    upper_line = []
    lower_line = []
    boll_bands = []
    median = moving_average(close_price, period)
    std_dev = standard_deviation(close_price, period)
    if len(median) > len(std_dev):
        median = median[-len(std_dev):]
    elif len(median) < len(std_dev):
        std_dev = std_dev[-len(median):]
    for i in range(len(std_dev)):
        upper_line.append(median[i] + (std_dev[i] * 2))
        lower_line.append(median[i] - (std_dev[i] * 2))
        boll_bands.append({'median': median[i],
                           'std dev': std_dev[i],
                           'upper line': median[i] + (std_dev[i] * 2),
                           'lower line': median[i] - (std_dev[i] * 2)})
    return boll_bands


# Donchian Channels


def donchian_channels(high_price, low_price, period):
    channels = []
    upper_band = []
    lower_band = []
    median = []
    for i in range(len(high_price)):
        up = max(high_price[i:i + period])
        low_price = min(low_price[i:i + period])
        median_line = (up + low_price) / 2
        upper_band.append(up)
        lower_band.append(low_price)
        median.append(median_line)
        channels.append({'upper band': up,
                         'median': median_line,
                         'lower band': low_price})
    return channels
