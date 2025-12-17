
class Botella:
    def __init__(self, marca, capacidad, tapa):
        self.marca = marca
        self.capacidad = capacidad
        self.tapa = tapa

    def llenar_botella(self,capacidad):
        print(f"la botella se llena con la siguiente cantidad:{capacidad}")
        print(f"Se va a usar la tapa para cerrar la botella:{self.tapa}")

    def cerrar_tapa(self, dato_cantidad):
        print(f"Se uso la tapa para cerrar la botella:{self.tapa}")
        print(f"Cantidad de tapas usadas:{dato_cantidad}")
        return dato_cantidad
    
    def imprimir_info(self):
        
        print(f"La marca de la botella es: {self.marca}")
        print(f"La capacidad de liquido que puede conterner la botella es de: {self.capacidad}")
        print(f"El tipo de tapa de la botella es: {self.tapa}")
        