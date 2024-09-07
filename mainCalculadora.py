# Importar modulos de calculadora
from calculadora import sumar,restar,multiplicar,dividir
# Importa modulo de tiempo
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
    
    # Espera unos segundos para desplegar el menú
    time.sleep(2)    
    
    # Despliega el menú
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
