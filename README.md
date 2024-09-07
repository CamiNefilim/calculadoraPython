# Calculadora Básica en Python

## Descripción

Este proyecto es una **calculadora básica** desarrollada en Python que permite realizar operaciones aritméticas fundamentales: suma, resta, multiplicación y división. Cada operación está implementada en módulos separados para facilitar la comprensión y el mantenimiento del código.

## Características

- **Modularidad**: Cada operación aritmética está encapsulada en su propio módulo.
- **Interfaz simple**: Interacción a través de la línea de comandos.
- **Fácil de entender**: Código claro y comentado, ideal para principiantes en Python.

## Requisitos

- Python 3.x instalado en tu sistema.

## Instalación

1. **Clonar el repositorio**

   ```bash
   git clone https://github.com/CamiNefilim/calculadoraPython.git
   ```

2. **Acceder al directorio del proyecto**

   ```bash
   cd calculadoraPython
   ```

## Uso

Ejecuta el script principal para iniciar la calculadora:

```bash
python mainCalculadora.py 
```
o

```bash
py mainCalculadora.py 
```

Sigue las instrucciones en pantalla para seleccionar la operación y proporcionar los números con los que deseas trabajar.

## Estructura del Proyecto

- `mainCalculadora.py`: Archivo principal que ejecuta la calculadora y maneja la interacción con el usuario.
- `calculadora/`  
  - `__init__.py`: Contiene la definión del paquete.
  - `suma.py`: Contiene la función para realizar sumas.
  - `resta.py`: Contiene la función para realizar restas.
  - `multiplicacion.py`: Contiene la función para realizar multiplicaciones.
  - `division.py`: Contiene la función para realizar divisiones.

## Ejemplo de Código

**mainCalculadora.py**

```python
#Importar modulos de calculadora
from calculadora import sumar,restar,multiplicar,dividir
#Importa modulo de tiempo
import time

def menu():
    print("Calculadora")
    print("""
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
    5. Salir
    """)

while True:
    
    #Espera unos segundos para desplegar el menú
    time.sleep(2)    
    
    #Despliega el menú
    menu()
    
    # Captura opción seleccionada
    opcion = input("Ingresa el número de la acción que deseas ejecutar: ")

    # Evalúa las opciones
    match opcion:
        case "1":
            # Si se selecciona 1. Sumar
            while True:
                try:
                    # Solicita números
                    valorA = float(input("Ingresa el primer número: "))
                    valorB = float(input("Ingresa el segundo número: "))
                    # Imprime resultado
                    print(f"La suma es: {sumar(valorA,valorB)}")
                    break  # Se sale del bucle si se ingresa número
                except ValueError:
                    # Imprime error
                    print("Para poder sumar se requiere ingresar números.")
        case "2":
            # Si se selecciona 2. Restar
            while True:
                try:
                    # Solicita números
                    valorA = float(input("Ingresa el primer número: "))
                    valorB = float(input("Ingresa el segundo número: "))
                    # Imprime resultado
                    print(f"La resta es: {restar(valorA,valorB)}")
                    break  # Se sale del bucle si se ingresa número
                except ValueError:
                    # Imprime error
                    print("Para poder restar se requiere ingresar números.")
        case "3":
            # Si se selecciona 3. Multiplicar
            while True:
                try:
                    # Solicita números
                    valorA = float(input("Ingresa el primer número: "))
                    valorB = float(input("Ingresa el segundo número: "))
                    # Imprime resultado
                    print(f"La multiplicación es: {multiplicar(valorA,valorB)}")
                    break  # Se sale del bucle si se ingresa número
                except ValueError:
                    # Imprime error
                    print("Para poder multiplicar se requiere ingresar números.")
        case "4":
            # Si se selecciona 4. Dividir
            while True:
                try:
                    # Solicita números
                    valorA = float(input("Ingresa el primer número: "))
                    valorB = float(input("Ingresa el segundo número: "))
                    #Verifica que el divisor no sea 0
                    if valorB == 0:
                        print("Para poder dividir se requiere que el divisor NO sea 0.")
                    else:
                        # Imprime resultado
                        print(f"La división es: {dividir(valorA,valorB)}")
                        break  # Se sale del bucle si se ingresa número
                except ValueError:
                    # Imprime error
                    print("Para poder dividir se requiere ingresar números.")
        case "5":
            print("Muchas gracias por usar mi calculadora.")
            break
        case _:
            print("No existe la opción ingresada")
```

## Ejemplos de Uso

**Ejecutar una suma:**

```
Calculadora

1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Salir

Ingresa el número de la acción que deseas ejecutar: 1
Ingresa el primer número: 2
Ingresa el segundo número: 6
La suma es: 8.0
```

**Ejecutar una división:**

```
Calculadora

1. Sumar
2. Restar
3. Multiplicar
4. Dividir
5. Salir

Ingresa el número de la acción que deseas ejecutar: 4
Ingresa el primer número: 6
Ingresa el segundo número: 0
Para poder dividir se requiere que el divisor NO sea 0.
Ingresa el primer número: 4
Ingresa el segundo número: 5
La división es: 0.8
```

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar este proyecto, por favor sigue estos pasos:

1. Haz un **fork** del repositorio.
2. Crea una nueva rama (`git checkout -b mejora/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -m 'Agrega nueva funcionalidad'`).
4. Haz push a la rama (`git push origin mejora/nueva-funcionalidad`).
5. Abre un **Pull Request**.

## Autor

- **Camila Alvarado Astroza** - [CamiNefilim](https://github.com/CamiNefilim)

## Agradecimientos

- A los colaboradores que ayudan a mejorar este proyecto.
- A la comunidad de Python por su extensa documentación y apoyo.

