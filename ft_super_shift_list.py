def ft_slice_str(mass, start, stop):
    result_mass = []
    for i in range(start, stop):
        result_mass.append(mass[i])
    return result_mass


def ft_super_shift_list(mass, n):
    return ft_slice_str(mass, -n, 0) + ft_slice_str(mass, 0, -n)
