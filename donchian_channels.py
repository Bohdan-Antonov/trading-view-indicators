# Donchian Channels


def donchian_channels(high_price, low_price, period):
    channels = []
    upper_band = []
    lower_band = []
    median = []
    for i in range(len(high_price)):
        up = max(high_price[i:i + period])
        low = min(low_price[i:i + period])
        median_line = (up + low) / 2
        upper_band.append(up)
        lower_band.append(low)
        median.append(median_line)
        channels.append({'upper band': up,
                         'median': median_line,
                         'lower band': low})
    return channels
