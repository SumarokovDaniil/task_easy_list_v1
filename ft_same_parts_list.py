def ft_len(mass):
    count = 0
    for _ in mass:
        count += 1
    return count


def ft_same_parts_list(mass):
    for i in range(1, ft_len(mass)):
        if mass[i] > 0 and mass[i - 1] > 0 or \
                mass[i] < 0 and mass[i - 1] < 0:
            return True
    return False
