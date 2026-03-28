import pytest
from utils import suma

def test_suma():
    assert suma(2, 3) == 5
    assert suma(-2, 3) == 1
    assert suma(-2, -3) == -5