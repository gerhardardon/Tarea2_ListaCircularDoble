class nodo:
    def __init__(self,valor):
        self.valor=valor
        self.anterior=None
        self.siguiente=None

class lista:
    def __init__(self):
        self.primero=None
        self.ultimo=None

    def insert(self,valor):
        nuevo = nodo(valor)
        if (self.primero == None):
            self.primero=nuevo
        else:
            nuevo.anterior=self.ultimo
            nuevo.siguiente=self.primero
            self.ultimo.siguiente=nuevo
            self.primero.anterior=nuevo
        self.ultimo=nuevo

    def imprimir(self):
        aux=self.primero
        while(aux!=None):
            print(aux.valor)

            while(aux.siguiente==self.primero):
                return
            
            aux=aux.siguiente
    
    def buscar(self,valor):
        aux=self.primero
        while(aux!=None):
            if (aux.valor==valor):
                print("\nencontrado\nanterior:",aux.anterior.valor,"actual:",aux.valor,"siguiente:",aux.siguiente.valor)
            while(aux.siguiente==self.primero):
                return
            aux=aux.siguiente

x=lista()
x.insert(1)
x.insert(2)
x.insert(3)
x.insert(4)
x.insert(5)

print("\nGerhard Ardon 202004796\nLista de números:")
x.imprimir()
print("Ingrese valor:")
num=input()
x.buscar(int(num))