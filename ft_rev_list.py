def ft_len(mass):
    count = 0
    for _ in mass:
        count += 1
    return count


def ft_rev_list(mass):
    for i in range(ft_len(mass)):
        mass[i] = ft_len(mass) - i
    return mass
