import pytest
from isTriangle import Triangle

def test_triangle_classification():
  #Tests for a given side being zero or negative
  assert Triangle.classify(0, 5, 5) == Triangle.Type.INVALID
  assert Triangle.classify(5, 0, 5) == Triangle.Type.INVALID 
  assert Triangle.classify(5, 5, 0) == Triangle.Type.INVALID
  assert Triangle.classify(-1, 5, 5) == Triangle.Type.INVALID 
  assert Triangle.classify(5, -1, 5) == Triangle.Type.INVALID 
  assert Triangle.classify(5, 5, -1) == Triangle.Type.INVALID
    
  #Tests for Scalene Triangle (a,b,c do not equal each other)
  assert Triangle.classify(3, 4, 5) == Triangle.Type.SCALENE
  assert Triangle.classify(5, 7, 10) == Triangle.Type.SCALENE   
    
  #Tests for Invalid Triangle (fails triangle inequality)
  assert Triangle.classify(1, 2, 10) == Triangle.Type.INVALID
  assert Triangle.classify(1, 10, 2) == Triangle.Type.INVALID 
  assert Triangle.classify(10, 1, 2) == Triangle.Type.INVALID
    
  #Tests for Equilateral Triangle (a=b=c)
  assert Triangle.classify(5, 5, 5) == Triangle.Type.EQUILATERAL
  assert Triangle.classify(10, 10, 10) == Triangle.Type.EQUILATERAL
    
  #Tests for Isosceles Triangle (exactly two sides equal)
  assert Triangle.classify(5, 5, 3) == Triangle.Type.ISOSCELES
  assert Triangle.classify(5, 3, 5) == Triangle.Type.ISOSCELES
  assert Triangle.classify(3, 5, 5) == Triangle.Type.ISOSCELES
    
  #Tests for Invalid Isosceles (violates triangle inequality but two sides are equal)
  assert Triangle.classify(1, 1, 3) == Triangle.Type.INVALID
  assert Triangle.classify(1, 3, 1) == Triangle.Type.INVALID 
  assert Triangle.classify(3, 1, 1) == Triangle.Type.INVALID  

#This allows the test file to be run using "python test_decisionCoverage.py" when the file is run as a script
if __name__ == '__main__': 
  pytest.main(['-v'])
