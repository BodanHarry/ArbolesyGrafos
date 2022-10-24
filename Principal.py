from Clases import Arbol 


arbol = Arbol("Luis")
arbol.agregar("María Jose")
arbol.agregar("Maggie")
arbol.agregar("Leon")
arbol.agregar("Cuphead")
arbol.agregar("Aloy")
arbol.agregar("Jack")
nombre = input("Ingrese el valor")
arbol.agregar(nombre)
arbol.preOrden()
arbol.enOrden()
arbol.postOrden()
