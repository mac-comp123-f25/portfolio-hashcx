import math


def estimate_green_roof(wid, len, sqf_cost):
    area = rect_area(wid, len)
    cost = roof_cost(area, sqf_cost)
    print(" Area = ", area)
    print(" Cost = ", cost)


def rect_area(w, l):
    return math.ceil(w) * math.ceil(l)


def roof_cost(area, cost_sqf):
    return area * cost_sqf


estimate_green_roof(54.25, 32.8, 35)
