import requests
import pandas


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
