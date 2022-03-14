# Primer Proyecto 
# En este proyecto va de comprovar si el numero que el usuario a registrado es par o impar 



print("*** Bienvenido a Par o Impar ***")
print()
a = int(input("Ingrese un numero del 1 al 1000  "))


if a >=1000:
        print("error")
elif a % 2 == 0:
     print("El numero es par !!!")
else:
    print("El numero es impar !!! ¿Pruebas con otro numero?")



