numeros = []
intentos = 0  # Contador para entradas válidas

while intentos < 3:
    numero = input('Ingrese un número (o "exit" para salir): ')
    
    if numero.lower() == "exit":
        break
    
    # Verifica si el número no está ya en la lista y es válido
    if numero not in numeros:
        numeros.append(numero)
        intentos += 1  # Solo aumenta si el número es válido
    else:
        print('El número ya se encuentra en la lista. Intente con otro número.')

    print("Números ingresados:", numeros)
