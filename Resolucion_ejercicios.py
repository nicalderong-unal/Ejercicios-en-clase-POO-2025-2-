#Autor: Nicolas Alexander Calderon Garcia
#Resolucion de ejercicios de programacion en python

#Ejercicio 15:
def cuadrados(limite):
    for i in range (1,limite+1):
        print(i,"*",i,"=",i**2)
limite=int(input("Ingrese el número límite a sacarle su cuadrado: "))
cuadrados(limite)
print()

#Ejercicio 16:
def multiplicatoria(limite):
    resultado=1
    for i in range (1,limite+1):
        resultado*=i
    return resultado
limite=int(input("Ingrese el número máximo para sacar su multiplicatoria: "))
print("El resultado de la multiplicatoria es: ",multiplicatoria(limite),"\n")

#Ejercicio 17:
def sumatoria_cuadrados(limite):
    resultado=0
    for i in range (1,limite+1):
        resultado+=i**2
    return resultado
limite=int(input("Ingrese el número máximo para sacar la sumatoria de sus cuadrados: "))
print("El resultado de la sumatoria de los cuadrados es: ",sumatoria_cuadrados(limite),"\n")

#Ejercicio 22: