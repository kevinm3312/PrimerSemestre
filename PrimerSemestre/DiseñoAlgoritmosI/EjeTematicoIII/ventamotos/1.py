def sistema_de_venta_motocicletas():
    # Solicitar datos al usuario
    try:
        precio_base = float(input("Ingrese el precio base de la motocicleta: "))
        marca = input("Ingrese la marca de la motocicleta (Honda, Yamaha, Suzuki, u Otra): ").capitalize()
        es_feriado = input("¿El día de la compra es feriado? (s/n): ").lower() == 's'
        dia = input("Ingrese el día de la semana (por ejemplo, 'Martes', 'Sábado'): ").capitalize()
    except ValueError:
        print("Error: Por favor, ingrese valores válidos.")
        return

    # Definir descuentos por marca
    descuentos_marca = {
        "Honda": 0.05,
        "Yamaha": 0.08,
        "Suzuki": 0.10,
        "Otra": 0.02
    }

    # Calcular descuento por marca
    descuento_marca = descuentos_marca.get(marca, 0.02)  # Descuento del 2% si la marca es "Otra"
    
    # Definir descuentos adicionales por día
    descuento_dia = 0
    if es_feriado:
        descuento_dia = 0.25
    elif dia == "Martes":
        descuento_dia = 0.12
    elif dia == "Sábado":
        descuento_dia = 0.18

    # Calcular descuento total aplicable (con límite del 30%)
    descuento_total = min(descuento_marca + descuento_dia, 0.30)

    # Calcular precios finales
    ahorro_total = precio_base * descuento_total
    precio_final = precio_base - ahorro_total

    # Mostrar desglose
    print("\n--- Desglose de la compra ---")
    print(f"Precio base: {precio_base:.2f}")
    print(f"Descuento por marca ({marca}): {descuento_marca * 100}%")
    print(f"Descuento adicional por día ({'Feriado' if es_feriado else dia}): {descuento_dia * 100}%")
    print(f"Descuento total aplicado (límite del 30%): {descuento_total * 100}%")
    print(f"Ahorro total: {ahorro_total:.2f}")
    print(f"Precio final de la motocicleta: {precio_final:.2f}")

sistema_de_venta_motocicletas()
