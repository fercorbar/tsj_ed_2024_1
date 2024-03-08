class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def consultar_lista(self):
        if self.head: # Si hay al menos un nodo
            texto = "(HEAD) "
            nodo_actual = self.head
            while(nodo_actual):
                texto += f"{nodo_actual.data} -> "
                nodo_actual = nodo_actual.next
            texto += "(null)"
            print(texto)
        else:
            print("La lista está vacía")

    def agregar_nodo_inicio(self, data):
        new_node = Node(data)
        if self.head == None: # Si no hay nodos
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def agregar_nodo_final(self, data):
        new_node = Node(data)
        if self.head == None: # Si no hay nodos
            self.head = new_node
        else:
            nodo_actual = self.head
            while(nodo_actual.next):
                nodo_actual = nodo_actual.next
            ultimo_nodo = nodo_actual
            ultimo_nodo.next = new_node

    def eliminar_nodo_inicio(self):
        if self.head: # Si hay al menos un nodo
            self.head = self.head.next
        else:
            print("La lista está vacía")

    def eliminar_nodo_final(self):
        if self.head: # Si al menos hay un nodo
            if self.head.next: # Si al menos hay 2 nodos
                nodo_actual = self.head
                while(nodo_actual.next.next):
                    nodo_actual = nodo_actual.next
                penultimo_nodo = nodo_actual
                penultimo_nodo.next = None
            else:
                self.head = None
        else: # si no hay ningun nodo
            print("La lista está vacía")




    # def actualizar_nodo_con_valor(self, valor_viejo, valor_nuevo): # Ejemplo cambiar valor de "C" a "CASA"
        
    #     # Código aquí


    # def eliminar_nodo_con_valor(self, valor): # Ejemplo eliminar nodo con valor "C"
        
    #     # Código aquí

    def actualizar_nodo_con_valor(self, valor_viejo, valor_nuevo):
        if self.head: #si tiene almenos un nodo
            nodo_actual = self.head
            while(nodo_actual):
                if nodo_actual.data == valor_viejo:
                    nodo_actual.data = valor_nuevo
                    break
                nodo_actual = nodo_actual.next 

    def eliminar_nodo_convalor(self, valor):
        if self.head:
            if self.head.data == valor:
                self.head = self.head.next
            else:
                nodo_actual = self.head
                while(nodo_actual.next):
                    if nodo_actual.next.data == valor:
                        nodo_actual.next = nodo_actual.next.next
                        break 
                    nodo_actual = nodo_actual.next
        else:
            print("La lista esta vacia")




mi_lista = LinkedList()
mi_lista.consultar_lista()
mi_lista.agregar_nodo_final("A")
mi_lista.agregar_nodo_final("B")
mi_lista.agregar_nodo_final("C")
mi_lista.consultar_lista()
mi_lista.agregar_nodo_final("D")
mi_lista.consultar_lista()
# mi_lista.eliminar_nodo_final()
# mi_lista.consultar_lista()
mi_lista.actualizar_nodo_con_valor("C", "Casa")
mi_lista.consultar_lista()
mi_lista.eliminar_nodo_convalor("D")
mi_lista.consultar_lista()