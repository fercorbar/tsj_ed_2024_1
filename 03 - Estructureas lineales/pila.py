class Pila:
    def __init__(self, tamano_max):
        self.tamano_max = tamano_max
        self.apuntador = 0
        self.cant_val_apilados = 0
        self.__arreglo = []

    def apilar(self, valor):
        if self.cant_val_apilados == self.tamano_max:
            print("No se puede apilar, la pila se encuentra llena.")
        else:
            self.__arreglo.append(valor)
            self.cant_val_apilados += 1
            self.apuntador +=1 

    def desapilar(self):
        if self.esta_vacia():
            print("No se puede desapilar, la pila está vacía.")
            return None
        else:
            valor = self.__arreglo.pop(self.apuntador-1)
            self.cant_val_apilados -= 1
            self.apuntador -= 1
            return valor
    
    def consultar(self):
        if self.esta_vacia():
            print("No se puede consultar, la pila está vacía.")
            return None
        else:
            return self.__arreglo[self.apuntador-1]
    
    def esta_vacia(self):
        if self.cant_val_apilados == 0:
            return True
        else:
            return False


mi_pila = Pila(6)
mi_pila.consultar()

mi_pila.apilar("S")
mi_pila.apilar("I")
mi_pila.apilar("L")
mi_pila.apilar("O")
mi_pila.apilar("H")
mi_pila.apilar("B")

print(mi_pila.desapilar())
print(mi_pila.desapilar())
print(mi_pila.desapilar())
print(mi_pila.desapilar())
print(mi_pila.desapilar())

mi_pila.consultar()
