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
