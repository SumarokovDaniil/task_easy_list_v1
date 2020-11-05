def ft_rshift_list(mass):
    new_mass = list()
    new_mass.append(mass[-1])
    for i in range(len(mass) - 1):
        new_mass.append(mass[i])
    return new_mass
