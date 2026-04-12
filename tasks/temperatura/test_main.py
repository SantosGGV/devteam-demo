from main import convertir_temperatura, obtener_temperatura_celsius, obtener_temperatura_fahrenheit, obtener_temperatura_kelvin
import pytest

def test_convertir_temperatura():
    assert convertir_temperatura(0, 'C', 'F') == 32.0
    assert convertir_temperatura(0, 'C', 'K') == 273.15
    assert convertir_temperatura(32, 'F', 'C') == 0.0
    assert convertir_temperatura(32, 'F', 'K') == 273.15
    assert convertir_temperatura(273.15, 'K', 'C') == 0.0
    assert convertir_temperatura(273.15, 'K', 'F') == 32.0

def test_obtener_temperatura_celsius():
    assert obtener_temperatura_celsius(0, 'C') == 0
    assert obtener_temperatura_celsius(32, 'F') == 0
    assert obtener_temperatura_celsius(273.15, 'K') == 0

def test_obtener_temperatura_fahrenheit():
    assert obtener_temperatura_fahrenheit(32, 'F') == 32
    assert obtener_temperatura_fahrenheit(0, 'C') == 32
    assert obtener_temperatura_fahrenheit(273.15, 'K') == 32

def test_obtener_temperatura_kelvin():
    assert obtener_temperatura_kelvin(273.15, 'K') == 273.15
    assert obtener_temperatura_kelvin(0, 'C') == 273.15
    assert obtener_temperatura_kelvin(32, 'F') == 273.15

def test_convertir_temperatura_invalida():
    assert convertir_temperatura(0, 'C', 'X') == "Unidades no válidas"

def test_obtener_temperatura_celsius_invalida():
    with pytest.raises(ValueError):
        obtener_temperatura_celsius(0, 'X')

def test_obtener_temperatura_fahrenheit_invalida():
    with pytest.raises(ValueError):
        obtener_temperatura_fahrenheit(0, 'X')

def test_obtener_temperatura_kelvin_invalida():
    with pytest.raises(ValueError):
        obtener_temperatura_kelvin(0, 'X')