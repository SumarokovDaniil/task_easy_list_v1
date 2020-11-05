def ft_rev_par_list(mass):
    if len(mass) % 2 == 0:
        for i in range(0, len(mass), 2):
            mass[i], mass[i + 1] = mass[i + 1], mass[i]
    for i in range(0, len(mass) - 1, 2):
        mass[i], mass[i + 1] = mass[i + 1], mass[i]
    return mass
