def ft_rshift_list(mass):
    first = mass[-1]
    for i in range(len(mass) - 1, 0, -1):
        mass[i] = mass[i - 1]
    mass[0] = first
    return mass


def ft_super_shift_list(mass, n):
    if n < 0:
        for i in range(len(mass) + n):
            mass = ft_rshift_list(mass)
        return mass
    else:
        for i in range(n):
            mass = ft_rshift_list(mass)
        return mass
