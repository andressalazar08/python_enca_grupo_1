'''
crear las funciones suma, resta, 
multiplicacion, división (validar 0 denominador),
división piso
crear una función que genere un número aleatorio 
(import random)
crear una función operación módulo (%)

'''
import random

def sumar(a,b):
    return a+b

def restar(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def dividir(a,b):
    if b==0:
        return "no se puede dividir en cero" 
    return a/b

def division_piso(a,b):
    return a//b

def numero_aleatorio():
    return round(random.random(),2)

def numero_modulo(a,b):
    return a%b