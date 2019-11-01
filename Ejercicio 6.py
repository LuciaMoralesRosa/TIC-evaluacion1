def ejercicio_6():
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
        resultado = x / float(y)
        print "El resultado a la operacion", x, "/", y, "es igual a", resultado
        
ejercicio_6()


    
