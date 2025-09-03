#Autor: Nicolas Alexander Calderon Garcia
#Resolucion de ejercicios de programacion en python

#Ejercicio 15:
def cuadrados():
    print()
    limite=int(input("Ingrese el número límite a sacarle su cuadrado: "))
    for i in range (1,limite+1):
        print(i,"*",i,"=",i**2)
cuadrados()

#Ejercicio 16:
def multiplicatoria():
    print()
    resultado=1
    limite=int(input("Ingrese el número máximo para sacar su multiplicatoria: "))
    for i in range (1,limite+1):
        resultado*=i
    print("El resultado de la multiplicatoria es: ",resultado)
multiplicatoria()

#Ejercicio 17:
def sumatoria_cuadrados():
    print()
    limite=int(input("Ingrese el número máximo para sacar la sumatoria de los cuadrados: "))
    resultado=0
    for i in range (1,limite+1):
        resultado+=i**2
    print("El resultado de la sumatoria de los cuadrados es: ",resultado)
sumatoria_cuadrados()

#Ejercicio 21:
def comparar_numeros():
    print()
    num1=int(input("Ingrese el primer número: "))
    num2=int(input("Ingrese el segundo número: "))
    if num1>num2:
        print("El primer número es mayor que el segundo")
    elif num1<num2:
        print("El segundo número es mayor que el primero")
    else:
        print("Los dos números son iguales")
comparar_numeros()

#Ejercicio 22:
def impares_menores():
    print()
    num=int(input("Ingrese un número para imprimir todos los impares menores a este: "))
    if num%2==0:
        num-=1
        for i in range (1,num+1,2):
            print(i)
    else:
        num-=2
        for i in range (1,num+1,2):
            print(i)
impares_menores()

#Ejercicio 26 (comparar tres números):
def comparar_tres_numeros():
    print()
    num1=int(input("Ingrese el primer número: "))
    num2=int(input("Ingrese el segundo número: "))
    num3=int(input("Ingrese el tercer número: "))   
    mayor=num1
    menor=num1
    if num2>mayor:
        mayor=num2
    else: menor=num2
    if num3>mayor:
        mayor=num3
    else: menor=num3
    print("El número mayor es: ",mayor)
    print("El número menor es: ",menor)
comparar_tres_numeros()
