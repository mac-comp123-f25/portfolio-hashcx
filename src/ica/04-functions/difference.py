def smallest_diff(x, y, z):
    diff1 = abs(x - y)
    diff2 = abs(y - z)
    diff3 = abs(x - z)
    min_diff = min(diff1, diff2, diff3)
    return min_diff


"""
Local Variable
x = 10
y =  20
z = 30
diff1 = 10
diff2 = 10
diff3 = 20
min_diff = 10
"""
print(smallest_diff(10, 20, 30))

"""
Local Variable
x = 2
y =  20
z = 20
diff1 = 18
diff2 = 0
diff3 = 18
min_diff = 0
"""
print(smallest_diff(2, 20, 20))
