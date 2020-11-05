def ft_len(mass):
    count = 0
    for _ in mass:
        count += 1
    return count


def ft_rshift_list(mass):
    first = mass[-1]
    for i in range(ft_len(mass) - 1, 0, -1):
        mass[i] = mass[i - 1]
    mass[0] = first
    return mass
