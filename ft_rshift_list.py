def ft_rshift_list(mass):
    c = mass[-1]
    for i in range(len(mass) - 1, 0, -1):
        mass[i] = mass[i - 1]
    mass[0] = c
    return mass
