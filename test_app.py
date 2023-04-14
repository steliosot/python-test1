import pytest

from app import addTwo

def test_add_positive():
  assert addTwo(1,2) == 3

def test_add_zero():
  assert addTwo(0,0) == 0

def test_negative():
  assert addTwo(10,-3) == 7

def test_string__expect_exception():
  with pytest.raises(TypeError):
    addTwo(10,'a')
