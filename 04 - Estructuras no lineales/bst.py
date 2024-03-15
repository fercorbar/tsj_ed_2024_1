class Node:
    def __init__(self, id):
        self.id = id
        self.left = Bst()
        self.right = Bst()

class Bst:
    def __init__(self):
        self.root = None
        
    def insert(self, id):
        if self.root == None:
            new_node = Node(id)
            self.root = new_node
        else:
            if id == self.root.id:
                print("Id ya existe en el árbol")
                return
            if id > self.root.id:
                self.root.right.insert(id)
            if id < self.root.id:
                self.root.left.insert(id)


mi_arbol = Bst()
mi_arbol.insert(8)
mi_arbol.insert(6)
mi_arbol.insert(9)
mi_arbol.insert(5)
mi_arbol.insert(15)
mi_arbol.insert(1)
mi_arbol.insert(4)
mi_arbol.insert(6)

print("OK")



