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

def test_scalene():
  assert Triangle.classify(3, 4, 5) == Triangle.Type.SCALENE
  #tests that triangle is scalene

def test_isosceles():
  assert Triangle.classify(4, 4, 6) == Triangle.Type.ISOSCELES
  assert Triangle.classify(3, 5, 3) == Triangle.Type.ISOSCELES
  assert Triangle.classify(7, 5, 5) == Triangle.Type.ISOSCELES
  #tests that triangle is isosceles (for different values of a,b,c)

def test_equilateral():
  assert Triangle.classify(3, 3, 3) == Triangle.Type.EQUILATERAL
  #tests that triangle is equilateral (a=b=c)


