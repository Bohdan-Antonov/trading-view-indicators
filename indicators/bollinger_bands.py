import sma
import standard_deviation


def bollinger_bands(close_price, period):
    upper_line = []
    lower_line = []
    boll_bands = []
    median = sma.moving_average(close_price, period)
    std_dev = standard_deviation.std_dev(close_price, period)
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
