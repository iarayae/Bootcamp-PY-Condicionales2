from string import ascii_lowercase
from getpass import getpass

# Ingreso de palabra secreta
while True:
    palabra_secreta = getpass("Ingresa una palabra secreta (solo letras, sin ñ, tildes ni números): ").lower()
    if all(letra in ascii_lowercase for letra in palabra_secreta):
        break
    else:
        print("Palabra inválida. Usa solo letras del abecedario inglés sin tildes ni símbolos.")

# Inicio del conteo de intentos
intentos = 0
descubierta = ""

for letra in palabra_secreta:
    for intento_letra in ascii_lowercase:
        intentos += 1
        if intento_letra == letra:
            descubierta += intento_letra
            print(f"Letra descubierta: {intento_letra}")
            break

print(f"Palabra descubierta: {descubierta}")
print(f"Total de intentos: {intentos}")
