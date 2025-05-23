print("Guía de Primeros Auxilios - Paso a Paso\n")

respuesta = input("¿La persona responde a estimulos? (si/no): ").lower()

if respuesta == "si":
    print("Valorar llevar a la persona al hospital más cercano.")
else:
    print("Abrir la vía aérea")
    respira = input("¿La persona respira? (si/no): ").lower()
    if respira == "si":
        print("Colocar en posición de suficiente ventilación.")
    else:
        print("Administrar 5 ventilaciones y llamar a una ambulancia.")
        ambulancia_llego = False
        while not ambulancia_llego:
            signos = input("¿La persona presenta signos de vida? (si/no): ").lower()
            if signos == "si":
                print("Reevaluar periódicamente mientras llega la ambulancia.")
            else:
                print("Administrar compresiones torácicas hasta que llegue ayuda.")
            ambulancia = input("¿La ambulancia ha llegado? (si/no): ").lower()
            if ambulancia == "si":
                ambulancia_llego = True
                print("Fin del proceso.")