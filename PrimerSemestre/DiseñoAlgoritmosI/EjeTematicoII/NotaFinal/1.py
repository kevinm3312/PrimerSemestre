def main():
    pesos = {
        'taller1': 0.20, 
        'taller2': 0.15, 
        'cuestionario1': 0.22, 
        'cuestionario2': 0.10, 
        'proyecto_final': 0.36
    }

    while True:
        try:
            
            notas = {k: float(input(f'Ingresa la nota del {k.capitalize()}: ')) for k in pesos}
            nota_final = sum(notas[k] * pesos[k] for k in pesos)
        
        except ValueError:
            print('Error: Dato Inválido')
            continue
        
        
        if 1.0 <= nota_final < 2.9:
            calificacion = 'Bajo'
        elif 2.9 <= nota_final < 4.0:
            calificacion = 'Básico'
        elif 4.0 <= nota_final <= 5.0:
            calificacion = 'Superior'
        else:
            print('Ingresa notas entre el rango de 1.0 a 5.0')
            continue
        
        print(f'Calificación: {calificacion}\nNota final: {nota_final:.2f}')
        
        # Preguntar si desea realizar otro cálculo
        if input('¿Deseas ingresar otro conjunto de notas? (s/n): ').strip().lower() != 's':
            print('Programa terminado.')
            break


main()
