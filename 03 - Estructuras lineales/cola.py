class Cola:
    def __init__(self, max):
        self.max = max
        self.puntero_cabeza =0
        self.puntero_fin= 0
        self.cantidad_valores_encolados =0
        self.__arreglo= [None]* self.max

    def encolar(self, valor):
        if self.esta_llena() == True:
            print("No se puede encolar, la cola está llena")
            return None
        else:
            self.__arreglo[self.puntero_fin]=valor
            self.cantidad_valores_encolados +=1

            if self.puntero_fin == self.max - 1:
                self.puntero_fin = 0
            else:
                self.puntero_fin +=1

            return valor

    def desencolar(self):
        if self.esta_vacia():
            print("no se puede desencolar; la cola esta vacia")
            return None
        else:
            valor = self.__arreglo[self.puntero_cabeza]
            self.__arreglo[self.puntero_cabeza] = None
            self.cantidad_valores_encolados -= 1
            if self.puntero_cabeza == self.max - 1:
                self.puntero_cabeza = 0
            else:
                self.puntero_cabeza += 1
            
            return valor
        
    def consultar(self, completo=False):
        if completo:
            texto = ""
            for element in self.__arreglo:
                if texto == "":
                    texto = str(element)
                else:
                    texto += " - " + str(element)
            print(texto)
        else:
            if self.esta_vacia():
                print("no se puede consultar, la cola esta vacia")
            else:
                print(self.__arreglo[self.puntero_cabeza])
        
    def esta_vacia(self): 
        if self.cantidad_valores_encolados == 0:
            return True
        else:
            return False
        
    def esta_llena(self):
        if self.cantidad_valores_encolados == self.max:
            return True
        else:
            return False


#pavo=Cola (5)
#print(pavo.encolar ("pizza"))

mi_cola = Cola(5)
mi_cola.consultar(completo=True)
mi_cola.consultar()
mi_cola.encolar("a")
mi_cola.encolar("b")
mi_cola.encolar("c")
mi_cola.encolar("d")
mi_cola.encolar("e")
mi_cola.consultar(completo=True)
mi_cola.desencolar()
mi_cola.consultar(completo=True)
mi_cola.desencolar()
mi_cola.consultar(completo=True)
mi_cola.desencolar()
mi_cola.consultar(completo=True)
mi_cola.encolar("f")
mi_cola.consultar(completo=True)
mi_cola.encolar("g")
mi_cola.consultar(completo=True)
mi_cola.desencolar()
mi_cola.consultar(completo=True)
mi_cola.desencolar()
mi_cola.consultar(completo=True)
mi_cola.desencolar()
mi_cola.consultar(completo=True)
mi_cola.encolar("h")
mi_cola.consultar(completo=True)
mi_cola.encolar("i")
mi_cola.consultar(completo=True)
mi_cola.desencolar()
mi_cola.consultar(completo=True)
mi_cola.desencolar()
mi_cola.consultar(completo=True)