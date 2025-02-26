import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def potencia(a, b):
    return math.pow(a, b)

def raiz_cuadrada(a):
    return math.sqrt(a)

def logaritmo(a, base=math.e):
    return math.log(a, base)

def seno(a):
    return math.sin(math.radians(a))

def coseno(a):
    return math.cos(math.radians(a))

def tangente(a):
    return math.tan(math.radians(a))

def factorial(a):
    return math.factorial(a)

def mostrar_menu():
    print("\nSeleccione una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz Cuadrada")
    print("7. Logaritmo")
    print("8. Seno")
    print("9. Coseno")
    print("10. Tangente")
    print("11. Factorial")
    print("12. Salir")

def obtener_numero(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

def main():
    resultado = None
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la operación que desea realizar: ")

        if opcion == '12':
            print("Saliendo...")
            break

        if opcion in ['1', '2', '3', '4', '5']:
            if resultado is None:
                num1 = obtener_numero("Ingrese el primer número: ")
            else:
                num1 = resultado
            num2 = obtener_numero("Ingrese el segundo número: ")

        elif opcion in ['6', '7', '8', '9', '10', '11']:
            if resultado is None:
                num1 = obtener_numero("Ingrese el número: ")
            else:
                num1 = resultado

        if opcion == '1':
            resultado = suma(num1, num2)
        elif opcion == '2':
            resultado = resta(num1, num2)
        elif opcion == '3':
            resultado = multiplicacion(num1, num2)
        elif opcion == '4':
            resultado = division(num1, num2)
        elif opcion == '5':
            resultado = potencia(num1, num2)
        elif opcion == '6':
            resultado = raiz_cuadrada(num1)
        elif opcion == '7':
            base = obtener_numero("Ingrese la base del logaritmo (presione Enter para base e): ") or math.e
            resultado = logaritmo(num1, base)
        elif opcion == '8':
            resultado = seno(num1)
        elif opcion == '9':
            resultado = coseno(num1)
        elif opcion == '10':
            resultado = tangente(num1)
        elif opcion == '11':
            resultado = factorial(int(num1))

        print(f"Resultado: {resultado}")
        resultado = None  # Reiniciar el resultado para la siguiente operación

if __name__ == "__main__":
    main()