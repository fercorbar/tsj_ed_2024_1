class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def consultar_lista(self):
        if self.head:
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
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def agregar_nodo_final(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            nodo_actual = self.head
            while(nodo_actual.next):
                nodo_actual = nodo_actual.next
            ultimo_nodo = nodo_actual
            ultimo_nodo.next = new_node




mi_lista = LinkedList()
mi_lista.consultar_lista()
mi_lista.agregar_nodo_inicio("A")
mi_lista.agregar_nodo_inicio("B")
mi_lista.agregar_nodo_inicio("C")
mi_lista.consultar_lista()
mi_lista.agregar_nodo_final("D")
mi_lista.consultar_lista()