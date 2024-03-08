class Node:
    def __init__(self, data) :
        self.data = data
        self.next = None
        self.prev = None 

class LinKedListDouble:
    def __init__(self) :
        self.head = None
        self.tail = None

    def consultar_lista(self):
        if self.head:
            texto = "(HEAD)"
            nodo_actual = self.head
            while(nodo_actual):
                texto += f"{nodo_actual.data} -> "
                nodo_actual = nodo_actual.next
            texto += "(null) (TAIL)"
            return texto
        else:
            return "Vacía"

    def agregar_nodo_al_inicio(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node     

    def agregar_nodo_al_final(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def eliminar_nodo_inicio(self):
        if self.head:
            if self.head.next:
                self.head.next.prev = None
                self.head = self.head.next
            else:
                self.head = None
                self.tail = None

    def eliminar_nodo_final(self):
        if self.head:
            if self.tail.prev:
                self.tail.prev.next = None
                self.tail = self.tail.prev
            else:
                self.head = None
                self.tail = None


    def actualizar_nodo_con_valor(self , valor_viejo , valor_nuevo):
        if self.head:  #si tiene almenos un nodo
            nodo_actual = self.head
            while(nodo_actual):
                if nodo_actual.data ==valor_viejo:
                    nodo_actual.data = valor_nuevo
                    break
                nodo_actual = nodo_actual.next
        
    def eliminar_nodo_con_valor(self , valor):
        if self.head:
            if self.head.data == valor:
                self.head = self.head.next
                self.head.prev = None
            elif self.tail.data == valor:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                nodo_actual = self.head
                while(nodo_actual.next):
                    if nodo_actual.next.data  == valor:
                        nodo_actual.next= nodo_actual.next.next
                        break
                    nodo_actual = nodo_actual.next

class Pila:
    def __init__(self):
        self.__lista = LinKedListDouble()

    def apilar(self, valor):
        self.__lista.agregar_nodo_al_final(valor)

    def desapilar(self):
        if not self.__lista.head:
            print("No se puede desapilar, la pila está vacía.")
            return None
        else:
            valor = self.__lista.tail.data
            self.__lista.eliminar_nodo_final()
            return valor
        
    def consultar(self):
        if not self.__lista.head:
            print("La pila está vacía.")
            return None
        else:
            return self.__lista.consultar_lista()

class Cola:
    def __init__(self):
        self.__lista = LinKedListDouble()

    def encolar(self, valor):
        self.__lista.agregar_nodo_al_final(valor)
        return valor

    def desencolar(self):
        if not self.__lista:
            print("No se puede desencolar; la cola esta vacia")
            return None
        else:
            valor = self.__lista.head.data
            self.__lista.eliminar_nodo_inicio()
            return valor

    def consultar(self):
        if not self.__lista.head:
            print("La cola está vacía.")
            return None
        else:
            return self.__lista.consultar_lista()

# mi_pila = Pila()
# mi_pila.consultar()
# mi_pila.apilar("S")
# mi_pila.apilar("I")
# mi_pila.apilar("L")
# mi_pila.apilar("O")
# mi_pila.apilar("H")
# mi_pila.apilar("B")
# print(mi_pila.desapilar())
# print(mi_pila.desapilar())
# print(mi_pila.desapilar())
# print(mi_pila.desapilar())
# print(mi_pila.desapilar())
# print(mi_pila.desapilar())
# print(mi_pila.consultar())
        

mi_cola = Cola()
print(mi_cola.consultar())
print(mi_cola.consultar())
mi_cola.encolar("a")
mi_cola.encolar("b")
mi_cola.encolar("c")
mi_cola.encolar("d")
mi_cola.encolar("e")
print(mi_cola.consultar())
print(mi_cola.desencolar())
print(mi_cola.consultar())
print(mi_cola.desencolar())
print(mi_cola.consultar())
print(mi_cola.desencolar())
print(mi_cola.consultar())
mi_cola.encolar("f")
print(mi_cola.consultar())
mi_cola.encolar("g")
print(mi_cola.consultar())
print(mi_cola.desencolar())
print(mi_cola.consultar())
print(mi_cola.desencolar())
print(mi_cola.consultar())
print(mi_cola.desencolar())
print(mi_cola.consultar())
mi_cola.encolar("h")
print(mi_cola.consultar())
mi_cola.encolar("i")
print(mi_cola.consultar())
print(mi_cola.desencolar())
print(mi_cola.consultar())
print(mi_cola.desencolar())
print(mi_cola.consultar())