import pytest
from main import fair_sharer

a = [0, 1000, 800, 0]
b = {100, 1000, 0, 1000}
c = (0, 1000, 800, 0)


def test_num_iterations():
    assert fair_sharer(a, 1) == [100.0, 800.0, 900.0, 0]
    assert fair_sharer(a, 1.0) == [100.0, 800.0, 900.0, 0]
    assert fair_sharer(a, "1") == f"{test_num_iterations} muss eine Zahl sein!"
    assert fair_sharer(a, 200) == [449.99954707983215, 500.00035830954874, 400.00037106047796, 449.9997235501422]


def test_values():
    assert fair_sharer(a, 1) == [100.0, 800.0, 900.0, 0]
    assert fair_sharer(b, 1) == f"{b} muss eine Liste sein"
    assert fair_sharer(c, 1) == f"{c} muss eine Liste sein"