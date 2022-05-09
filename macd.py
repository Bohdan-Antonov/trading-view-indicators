import ema

def macd(close, fast=12, slow=26):
    ema_slow = ema.exponential_moving_average(close, slow)
    ema_fast = ema.exponential_moving_average(close, fast)[-len(ema_slow):]
    macd_line = []
    for i in range(len(ema_slow)):
        macd_line.append(ema_fast[i] - ema_slow[i])
    signal_line = ema.exponential_moving_average(macd_line, 9)
    macd_line = macd_line[-len(signal_line):]
    histogram = []
    for i in range(len(signal_line)):
        histogram.append(macd_line[i] - signal_line[i])
    return macd_line, signal_line, histogram
