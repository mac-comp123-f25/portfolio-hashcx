def sum3(lst):
    assert type(lst) in [list, tuple]
    assert len(lst) >= 3
    for i in range(3):
        assert type(lst[i]) in [int, float]

    total = 0
    for i in range(3):
        total += lst[i]

    return total


if __name__ == "__main__":
  print( sum3([5, 2, 8, -2, 6, 15]) )
  print( sum3([5, 2]) )
  print( sum3(5) )
  print( sum3(["h", "i", 1, 2, 3]) )
  print( sum3([1, 2, 3, "h", "i"]) )
