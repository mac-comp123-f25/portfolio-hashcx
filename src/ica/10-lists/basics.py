def every_other(lst: list[int]):
    return lst[0:len(lst):2]


def sum_positive(lst: list[int]):
    sum = 0
    for n in lst:
        if n > 0:
            sum += n

    return sum


print(every_other([1, 2, 3, 4, 5, 6, 7, 8]))
print(sum_positive([1, -2, -3, -4, -5, -6, -7, 8]))
