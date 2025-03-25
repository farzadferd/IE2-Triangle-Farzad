import pytest
from isTriangle import Triangle

def test_invalid_non_positive_sides():
    assert Triangle.classify(0, 4, 5) == Triangle.Type.INVALID
    assert Triangle.classify(3, -1, 5) == Triangle.Type.INVALID
    assert Triangle.classify(3, 4, -2) == Triangle.Type.INVALID

def test_triangle_inequality_invalid():
    assert Triangle.classify(1, 2, 3) == Triangle.Type.INVALID
    assert Triangle.classify(1, 3, 1) == Triangle.Type.INVALID
    assert Triangle.classify(5, 1, 2) == Triangle.Type.INVALID

def test_scalene_triangle():
    assert Triangle.classify(3, 4, 5) == Triangle.Type.SCALENE
    assert Triangle.classify(5, 6, 7) == Triangle.Type.SCALENE

def test_equilateral_triangle():
    assert Triangle.classify(5, 5, 5) == Triangle.Type.EQUILATERAL
    assert Triangle.classify(10, 10, 10) == Triangle.Type.EQUILATERAL

def test_isosceles_triangle():
    assert Triangle.classify(5, 5, 7) == Triangle.Type.ISOSCELES
    assert Triangle.classify(5, 5, 6) == Triangle.Type.ISOSCELES
    assert Triangle.classify(5, 7, 5) == Triangle.Type.ISOSCELES
    assert Triangle.classify(6, 7, 6) == Triangle.Type.ISOSCELES
    assert Triangle.classify(7, 5, 5) == Triangle.Type.ISOSCELES
    assert Triangle.classify(6, 5, 5) == Triangle.Type.ISOSCELES

def test_edge_cases():
    assert Triangle.classify(3, 3, 4) == Triangle.Type.ISOSCELES
    assert Triangle.classify(4, 3, 3) == Triangle.Type.ISOSCELES
    assert Triangle.classify(3, 4, 3) == Triangle.Type.ISOSCELES

#This allows the test file to be run using "python test_decisionCoverage.py" when the file is run as a script
if __name__ == '__main__': 
  pytest.main(['-v'])
