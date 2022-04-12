# En este proyecto o ejercicio introducimos un numero cualquiera y el programa se encarga de eliminar todos los numeros pares, en los numeros multipos de 3 y 5 imprime fizzBuzz 
n = int(input("Ingrese un numero: "))
for x in range(1, n,2):
    if x % 3 == 0 and x % 5 == 0 :
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)
        