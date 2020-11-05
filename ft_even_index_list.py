def ft_len(mass):
    count = 0
    for _ in mass:
        count += 1
    return count


def ft_even_index_list(mass):
    new_mass = list()
    for i in range(ft_len(mass)):
        if i % 2 == 0:
            new_mass.append(mass[i])
    return new_mass
