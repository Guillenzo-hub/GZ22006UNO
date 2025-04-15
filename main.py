from ecuaciones.gauss import eliminacion_gauss
from ecuaciones.gauss_jordan import gauss_jordan
from ecuaciones.cramer import cramer
from ecuaciones.lu import descomposicion_lu
from ecuaciones.jacobi import jacobi
from ecuaciones.gauss_seidel import gauss_seidel
from ecuaciones.biseccion import biseccion
import numpy as np

def imprimir_menu():
    print("Seleccione un método para resolver el sistema de ecuaciones:")
    print("1. Eliminación de Gauss")
    print("2. Gauss-Jordan")
    print("3. Cramer")
    print("4. Descomposición LU")
    print("5. Jacobi")
    print("6. Gauss-Seidel")
    print("7. Bisección")
    print("0. Salir")

def pedir_matriz_y_vector():
    n = int(input("Ingrese el número de ecuaciones (filas de la matriz): "))
    A = [];
    b = [];
    
    print("Ingrese los coeficientes de la matriz A:")
    for i in range(n):
        fila = list(map(float, input(f"Fila {i+1} de A: ").split()))
        A.append(fila);
    
    print("Ingrese el vector b:")
    b = list(map(float, input("Vector b: ").split()))
    
    return np.array(A), np.array(b)

def ejecutar():
    while True:
        imprimir_menu()
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            A, b = pedir_matriz_y_vector()
            solucion = eliminacion_gauss(A, b)
            print(f"Solución usando Eliminación de Gauss: {solucion}")
            break
        
        if opcion == 2:
            A, b = pedir_matriz_y_vector()
            solucion = gauss_jordan(A, b)
            print(f"Solución usando Gauss-Jordan: {solucion}")
            break

        if opcion == 3:
            A, b = pedir_matriz_y_vector()
            solucion = cramer(A, b)
            print(f"Solución usando Cramer: {solucion}")
            break

        if opcion == 4:
            A, b = pedir_matriz_y_vector()
            solucion = descomposicion_lu(A, b)
            print(f"Solución usando descompocicion LU: {solucion}")
            break

        if opcion == 5:
            A, b = pedir_matriz_y_vector()
            solucion = jacobi(A, b)
            print(f"Solución usando Jacobi: {solucion}")
            break

        if opcion == 6:
            A, b = pedir_matriz_y_vector()
            solucion = gauss_seidel(A, b)
            print(f"Solución usando Gauss-Seidel: {solucion}")
            break

        if opcion == 7:
            A, b = pedir_matriz_y_vector()
            solucion = biseccion(A, b)
            print(f"Solución usando Biseccion: {solucion}")
            break


        if opcion == 0:
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    ejecutar()
