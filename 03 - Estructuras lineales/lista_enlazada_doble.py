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
            print(texto)
        else:
            print("la lista esta vacia")

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
            self.head.next.prev = None
            self.head = self.head.next
        else:
            print("la lista esta vacia")

    def eliminar_nodo_final(self):
        if self.head:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        else:
            print("la lista esta vacia")

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
        else:
            print("la lista esta vacia ")   






mi_lista = LinKedListDouble()
mi_lista.consultar_lista()
mi_lista.agregar_nodo_al_inicio("A")
mi_lista.agregar_nodo_al_final("B")
mi_lista.agregar_nodo_al_final("C")
mi_lista.consultar_lista()
mi_lista.agregar_nodo_al_final("D")
mi_lista.consultar_lista()
#mi_lista.eliminar_nodo_final()
#mi_lista.consultar_lista()
mi_lista.actualizar_nodo_con_valor("C", "CASA")
mi_lista.consultar_lista()
mi_lista.eliminar_nodo_con_valor("D")
mi_lista.consultar_lista()