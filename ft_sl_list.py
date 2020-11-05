def ft_sl_list(mass):
    count = 0
    for i in range(1, len(mass)):
        if mass[i] > mass[i - 1]:
            count += 1
    return count
