from modelo_vehiculo import Vehiculo
from modelo_vehiculo_deportivo import Vehiculo_Deportivo
from modelo_vehiculo_transporte import Vehiculo_Transporte
from modelo_vehiculo_carga import Vehiculo_Carga

#VEHICULO DEPORTIVO 
objVehiculo_deportivo = Vehiculo_Deportivo(
    "BMW Z4 Roadster", "3.0L TwinPower Turbo (6 cilindros)","Gris metalico","""
""","""
- Boton Start/Stop
- Apagado automático si se aleja la llave (en algunos modelos)
""","Climatizador bizona automático","""
- Llave inteligente (Keyless)
"""
)
objVehiculo_deportivo.imprimir_informacion()

# VEHICULO TRANSPORTE 
objVehiculo_transporte = Vehiculo_Transporte(
    "JAC Sunray Passenger Van", "Blanco polar", "Motor 2.0L Turbo Diésel", """
- Llave tradicional
- Llave de proximidad (en algunos modelos)
- Encendido por giro
""","""
- Llave
- Giro manual en el switch
""","Aire acondicionado de cabina completa","""

"""
)
objVehiculo_transporte.imprimir_informacion()

# OBJETO CARGA 
objVehiculo_carga = Vehiculo_Carga(
    "JAC Heavy Duty Truck", "Blanco estándar", "Motor 3.8L Turbo Diésel","""
- Llave tradicional reforzada
- Encendido por giro
""", """

- Apagado manual por switch
""", "Aire acondicionado básico de cabina", """
- Cierre mecánico
- Barra antirrobo en volante (en algunos modelos)
"""
)
objVehiculo_carga.imprimir_informacion()


