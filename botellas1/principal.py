from modelo_botella import Botella
from modelo_botella_plastico import Botella_plastico
from modelo_botella_vidrio import Botella_vidrio

# codigo principal
objBotella = Botella("botella de agua cristal", "1.5L", "Especial")
objBotella.imprimir_info()

plastico_botella = Botella_plastico("botella cristal", "2.5L", "Comun", "cilindrica", "plastico", "sin color o sin tinte")
dato_botella_plastica = plastico_botella.imprimir_info()
print(dato_botella_plastica)

vidrio_botella = Botella_vidrio("manantial", "1.5L", "Comun", "triangular", "Vidrio", "colo azul")
dato_botella_vidrio = vidrio_botella.imprimir_info()
print(dato_botella_vidrio)