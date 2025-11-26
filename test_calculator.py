import pytest
from calculator import add, sub, mul, div

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0

def test_sub():
    assert sub(5, 3) == 2

def test_mul():
    assert mul(2, 3) == 6

def test_div():
    assert div(6, 3) == 2
    assert div(1, 3) == pytest.approx(0.333333, rel=1e-3)

def test_div_by_zero():
    with pytest.raises(ValueError):
        div(1, 0)
