
from modelo_botella import Botella

class Botella_vidrio(Botella):
    def __init__(self, marca, capacidad, tapa, diseño, material, tinte):
        super().__init__(marca, capacidad, tapa)
        self.diseño = diseño
        self.material = material
        self.tinte = tinte

    def reutilizar_botella(self):
        print(f"la botella se puede usar para el recilaje con su material de: {self.material}")

    def imprimir_info(self):
        super().imprimir_info()
        print(f"El diseño de la botella es: {self.diseño}")
        print(f"El material de la botella es: {self.material}")
        print(f"El color de la botella es: {self.tinte}")
        return "AQUI ESTA LA INFORAMCION DE LA BOTELLA"