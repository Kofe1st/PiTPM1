from PiTPM import Factorial
import pytest
def testing1():
    fact = Factorial()
    assert fact.factorial(2) == 2
def testing2(self):
    fact = Factorial()
    assert fact.factorial(3) == 6
def testing3():
    fact = Factorial()
    assert fact.factorial(4) == 24
def testing4():
    fact = Factorial()
    assert fact.factorial(5) == 120
if __name__ == "__main__":
    pytest.main()
