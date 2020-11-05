def ft_even_index_list(mass):
    new_mass = list()
    for i in range(len(mass)):
        if i % 2 == 0:
            new_mass.append(mass[i])
    return new_mass
