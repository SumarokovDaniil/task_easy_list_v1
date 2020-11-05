def ft_rev_list(mass):
    new_mass = []
    for i in range(-1, -len(mass) - 1, -1):
        new_mass.append(mass[i])
    return new_mass


def ft_rev_par_list(mass):
    new_mass = list()

    if len(mass) % 2 == 0:
        for i in range(1, len(mass), 2):
            new_mass.append(mass[i])
            new_mass.append(mass[i - 1])
        return ft_rev_list(new_mass)

    for i in range(1, len(mass), 2):
        new_mass.append(mass[i])
        new_mass.append(mass[i - 1])
    new_mass.append(mass[-1])
    return ft_rev_list(new_mass)
