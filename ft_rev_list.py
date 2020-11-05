def ft_rev_list(mass):
    for i in range(len(mass)):
        mass[i] = len(mass) - i
    return mass
