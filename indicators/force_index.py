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