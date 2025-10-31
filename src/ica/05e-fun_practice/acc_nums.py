def sum_range(start_val, end_val):
    cnt = 0
    for x in range(start_val, end_val + 1):
        cnt = cnt + x
    return cnt


print(sum_range(10, 20))
print(sum_range(10, 10))
print(sum_range(20, 10))
print(sum_range(-20, -10))
