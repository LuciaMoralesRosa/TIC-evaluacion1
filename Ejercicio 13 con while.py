#Escriba una función que imprima por pantalla una pirámide
def Ejercicio_13():
    print "Cree su piramide"
    x = raw_input ("Para ello inserte * a continuacion: ")
    while (x!="*"):
        print """Lo lamento, su piramide no se ha podido construir por falta de material
            Pruebe otra vez"""
        x = raw_input ("Para ello inserte * a continuacion: ")
    print """    *
   ***
  *****
 *******
*********"""        
Ejercicio_13()
