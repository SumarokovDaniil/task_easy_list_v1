def ft_len(mass):
    count = 0
    for _ in mass:
        count += 1
    return count


def ft_sl_list(mass):
    count = 0
    for i in range(1, ft_len(mass)):
        if mass[i] > mass[i - 1]:
            count += 1
    return count
