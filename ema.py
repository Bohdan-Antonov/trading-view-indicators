import sma

# Exponential Moving Average 

def exponential_moving_average(data, period):
    ma_list = sma.moving_average(data, period)
    multiplier = 2 / (period + 1)
    ema_values = []
    ema_start = (data[1] - ma_list[0]) * multiplier + ma_list[0]
    ema_values.append(ema_start)
    for i in range(len(data[2:])):
        ema_values.append((data[i+1] - ema_values[i]) * multiplier + ema_values[i])
    return ema_values
