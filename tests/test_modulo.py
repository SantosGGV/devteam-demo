import pytest
from modulo import convertir_temperatura

def test_convertir_celsius_a_fahrenheit():
    assert convertir_temperatura(0, 'C', 'F') == 32.0

def test_convertir_fahrenheit_a_celsius():
    assert convertir_temperatura(32, 'F', 'C') == 0.0

def test_convertir_celsius_a_celsius():
    assert convertir_temperatura(0, 'C', 'C') == 0.0

def test_convertir_fahrenheit_a_fahrenheit():
    assert convertir_temperatura(32, 'F', 'F') == 32.0
