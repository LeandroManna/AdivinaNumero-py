import random

# Declaración de variables
limiteInferior = int(input("Ingrese el límite inferior del rango: "))
limiteSuperior = int(input("Ingrese el límite superior del rango: "))
intentosMax = int(input("Ingrese la cantidad de intentos máximos: "))
ciclosDeIntentos = intentosMax
guesses = []
numGuesses = 0
guessedRight = False

# Generamos el número secreto aleatorio
numSecreto = random.randint(limiteInferior, limiteSuperior)

# Iniciamos el ciclo de intentos
while ciclosDeIntentos > 0 and not guessedRight:
    # Pedimos al usuario que ingrese un número
    numUsuario = int(input("Ingrese un número: "))

    # Verificamos si el número ya fue ingresado anteriormente
    if numUsuario in guesses:
        print("El número " + str(numUsuario) + " ya fue ingresado anteriormente.")
        continue

    # Agregamos el número al array de intentos
    guesses.append(numUsuario)
    numGuesses += 1

    # Ordenamos el array de intentos de manera ascendente
    guesses.sort()

    # Informamos los números ingresados anteriormente
    print("Números ingresados anteriormente: " + " ".join(str(num) for num in guesses))

    # Verificamos si el usuario adivinó el número secreto
    if numUsuario == numSecreto:
        print("¡Felicitaciones! Adivinaste el número secreto en " + str(intentosMax - ciclosDeIntentos + 1) + " intentos.")
        guessedRight = True
    else:
        # Informamos si el número ingresado es mayor o menor que el número secreto
        if numUsuario < numSecreto:
            print("El número ingresado es menor que el número secreto.")
        else:
            print("El número ingresado es mayor que el número secreto.")

        # Informamos cuántos intentos lleva y cuántos intentos le quedan al usuario
        print("Lleva " + str(intentosMax - ciclosDeIntentos + 1) + " intentos.")
        ciclosDeIntentos -= 1
        print("Le quedan " + str(ciclosDeIntentos) + " intentos.")

# Verificamos si se quedó sin intentos y le informamos el número secreto
if ciclosDeIntentos == 0:
    print("Se quedó sin intentos. El número secreto era: " + str(numSecreto) + ".")
