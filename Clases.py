from re import L


class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self, dato):
        self.raiz = Nodo(dato)

    def _agregarRecursivo(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self._agregarRecursivo(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self._agregarRecursivo(nodo.derecha, dato)

    def _enOrdenRecursivo(self, nodo):
        if nodo is not None:
            self._enOrdenRecursivo(nodo.izquierda)
            print(nodo.dato, end = " , ")
            self._enOrdenRecursivo(nodo.derecha)

    def _preOrdenRecursivo(self, nodo):
        if nodo is not None:
            print(nodo.dato, end = " , ")
            self._preOrdenRecursivo(nodo.izquierda)
            self._enOrdenRecursivo(nodo.derecha)

    def _postOrdenRecursivo(self, nodo):
        if nodo is not None:
            self._preOrdenRecursivo(nodo.izquierda)
            self._enOrdenRecursivo(nodo.derecha)
            print(nodo.dato, end = " , ")

    def _buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.dato == busqueda:
            return nodo
        if busqueda < nodo.dato:
            return self._buscar(nodo.izquierda, busqueda)
        else:
            return self._buscar(nodo.derecha, busqueda)

    def agregar(self, dato):
        self._agregarRecursivo(self.raiz, dato)

    def enOrden(self):
        print("Imprimiendo árbol in order")
        self._enOrdenRecursivo(self.raiz)
        print("")

    def preOrden(self):
        print("Imprimiendo árbol pre order")
        self._preOrdenRecursivo(self.raiz)
        print("")

    def postOrden(self):
        print("Imprimiendo árbol post order")
        self._postOrdenRecursivo(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self._buscar(self.raiz, busqueda)