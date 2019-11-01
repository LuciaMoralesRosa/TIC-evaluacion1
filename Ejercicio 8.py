def IVA():
    x = input ("Ingrese el precio al que aplicarle el IVA: ")
    y = raw_input ("Ingrese el tipo de IVA: ") 

    if(y == "general"):
        resultado = (x+x*0.16)
    if(y == "reducido"):
        resultado = (x+x*0.07)
    if(y == "superreducido"):
        resultado = (x+x*0.04)

    
    print "El precio final es de", resultado, "$"
IVA()
