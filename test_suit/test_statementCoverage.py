import pytest
from isTriangle import Triangle

def test_zero_sides():
  assert Triangle.classify(0,5,5) == Triangle.Type.INVALID
  assert Triangle.classify(2,0,0) == Triangle.Type.INVALID
  assert Triangle.classify(0,0,0) == Triangle.Type.INVALID
  #tests that triangle with one or more zero sides is invalid triangle

def test_negative_sides():
  assert Triangle.classify(-2,3,3) == Triangle.Type.INVALID
  assert Triangle.classify(-4,-4,4) == Triangle.Type.INVALID
  assert Triangle.classify(-1,-1,-1) == Triangle.Type.INVALID
  #tests that triangle with one or more negative sides is invalid triangle
