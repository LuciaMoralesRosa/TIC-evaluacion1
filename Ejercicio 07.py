def ejercicio_7():
    x = input ("Introduzca un numero: ")
    y = input ("Introduzca otro numero: ")
    print """Seleccione la operacion a realizar teniendo en cuenta lo siguiente:
            - S es suma
            - R es resta
            - M es multiplicacion
            - D es division"""
    
    z = raw_input ("Que operacion quiere realizar? ")

    if (z == "S"):
        resultado = x + y
        print "El resultado a la operacion", x, "+", y, "es igual a", resultado
    if (z == "R"):
        resultado = x - y
        print "El resultado a la operacion", x, "-", y, "es igual a", resultado
    if (z == "M"):
        resultado = x * y
        print "El resultado a la operacion", x, "*", y, "es igual a", resultado
    
        
    if (z == "D"):

        while (y == 0):
            if (y == 0):
                print """Error, ha introducido un 0.
    Por favor, introduzca otro numero"""
                y = input ("Introduzca el nuevo numero: ")
        else:
            resultado = x / float(y)
            print "El resultado a la operacion", x, "/", y, "es igual a", resultado
        
ejercicio_7()


    
