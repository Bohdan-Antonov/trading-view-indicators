import math


def std_dev(closep, period):
    std_dev_values = []
    for i in range(len(closep) - (period - 1)):
        mean = sum(closep[i:i + period]) / period
        dev = []
        dev_sq = []
        for x in closep[i:i + period]:
            dev.append((x - mean))
            dev_sq.append(abs(pow((x - mean), 2)))
        std_dev = math.sqrt((sum(dev_sq) / period))
        std_dev_values.append(std_dev)
    return std_dev_values
