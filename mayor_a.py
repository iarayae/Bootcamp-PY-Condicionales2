import sys

ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000
}

# Validación de argumento
if len(sys.argv) != 2:
    print("Uso: python mayor_a.py <umbral>")
    sys,exit(1)

# Convertir argumento a número
umbral = int(sys.argv[1])

# Filtrar ventas mayores al umbral
mayores = {mes: valor for mes, valor in ventas.items() if valor > umbral}

# Mostrar resultados
print(mayores)