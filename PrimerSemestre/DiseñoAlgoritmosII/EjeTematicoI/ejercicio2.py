lista = []

def add_num():
    try:
        while True:
            lista.append(input('Ingresa un numero: '))
            opcion = input('¿Desea continuar añadiendo numeros?(S/N): ').upper()
            if opcion == 'S':
                continue
            else:
                break

    except ValueError:
        print('Error: Ingresa un Dato numerico')


def main():
    add_num()
    listados = []
    for i in lista:
        if i not in listados:
            listados.append(i)
            
    
    print(listados)

main()