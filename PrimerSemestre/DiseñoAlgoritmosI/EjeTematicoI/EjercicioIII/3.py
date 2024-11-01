lista = []
x = 15
y = 10
nota1 = lista.append(input('Ingrese nota 1: '))
nota2 = lista.append(input('Ingrese nota 2: '))
nota3 = lista.append(input('Ingrese nota 3: '))
nota4 = lista.append(input('Ingrese nota 4: '))

promedio = sum(lista) / len(lista)

if promedio >= 0 and promedio <= 2.99:
    print('Nota Baja')
elif promedio >= 3 and promedio <= 3.99:
    print('Nota media')
elif promedio >= 4 and promedio <= 5:
    print('¡Felicidades! Obtuviste Una nota alta')
    print('Te has ganado un 20% en el valor de la martricula')
    precio_matricula = float(input("Ingresa el valor de la matricula: "))
    total = float(precio_matricula - (precio_matricula * 0.2))
    print(f"El precio de la matricula es {total}")
