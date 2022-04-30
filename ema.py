import sma


def exponential_moving_average(data, period):
    ma_list = sma.moving_average(data, period)
    multiplier = 2 / (period + 1)
    ema_list = []
    ema_start = (data[1] - ma_list[0]) * multiplier + ma_list[0]
    ema_list.append(ema_start)
    for i in range(len(data[2:])):
        ema_list.append((data[i+1] - ema_list[i]) * multiplier + ema_list[i])
    print(ema_list)
