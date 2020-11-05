def ft_even_parts_list(mass):
    new_mass = list()
    for number in mass:
        if number % 2 == 0:
            new_mass.append(number)
    return new_mass
