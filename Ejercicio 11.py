#Escribir una función llamada 'cantidad' que reciba como argumento un número
#entero y una palabra y que luego diga si la palabra tiene la misma cantidad de
#letras que el número entero enviado.
def Ejercicio_11():
    x = raw_input ("Introduzca un numero: ")
    y = raw_input ("Introduzca una palabra: ")
    print "Caracteres del numero:", len(x)
    print "Caracteres de la palabra:", len(y)
    z = len(x)==len(y)
    if (z==True):
        print "     La palabra", y, "tiene los mismos caracteres que el numero", x
    else:
        print "     La palabra", y, "tiene un numero distinto de caracteres que el numero", x

Ejercicio_11()
