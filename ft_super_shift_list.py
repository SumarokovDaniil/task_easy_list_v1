def ft_len(mass):
    count = 0
    for _ in mass:
        count += 1
    return count


def ft_rshift_list(mass):
    first = mass[-1]
    for i in range(len(mass) - 1, 0, -1):
        mass[i] = mass[i - 1]
    mass[0] = first
    return mass


def ft_super_shift_list(mass, n):
    if n > 0:
        for _ in range(n):
            mass = ft_rshift_list(mass)
        return mass
    else:
        for _ in range(ft_len(mass) + n):
            mass = ft_rshift_list(mass)
        return mass
