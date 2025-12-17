

from modelo_mamifero import Mamifero
from modelo_reptil import Reptil
from modelo_ave import Ave
from modelo_insecto import Insecto
from modelo_pez import Pez

print("\nMAMÍFERO ")
caballo = Mamifero("vaca", 5, "montañas", "Herbívoro", "Grande", "blanco y negro", "Pelaje corto")
caballo.imprimir_informacion()

print("REPTIL")
cocodrilo = Reptil("serpiente ", 12, "Ríos y pantanos", "omnivero", "Grande", "verde", "Escamas debiles")
cocodrilo.imprimir_informacion()

print("PEZ")
pez_cirujano = Pez("Pez payaso", 2, "Arrecifes", "Omnívoro", "Mediano", "naranja, blanco y negro", "Agua salada")
pez_cirujano.imprimir_informacion()

print("INSECTO ")
escarabajo = Insecto("salta montes", 1, "campos", "Detritívoro", "Pequeño", "verde", 6)
escarabajo.imprimir_informacion()

print("AVE")
pato = Ave("paloma ", 3, "arboles ", "Omnívoro", "Mediano", "Blanco o gris", "Pico puntiagudo")
pato.imprimir_informacion()