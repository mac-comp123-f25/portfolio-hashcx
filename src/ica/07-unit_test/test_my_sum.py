import pytest
from my_sum import *

def test_sum3_ints():
    assert sum3([5, 2, 8, -2, 6, 15]) == 15
    assert sum3([5, 2, 2]) == 9
    assert sum3([5, 5, 5]) == 15
