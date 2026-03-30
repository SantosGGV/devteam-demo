## Modulo de conversión de temperatura

Este modulo permite convertir temperatura de Celsius a Fahrenheit y viceversa.

### Ejemplo de uso

```python
from modulo import convertir_temperatura

print(convertir_temperatura(30, 'C'))  # Salida: (86.0, 'F')
print(convertir_temperatura(86, 'F'))  # Salida: (30.0, 'C')
```

### Función convertir_temperatura

La función convertir_temperatura toma dos argumentos: grados y unidad. La función devuelve una tupla con la temperatura convertida y la unidad de medida.

### Unidades de medida

- C: Celsius
- F: Fahrenheit