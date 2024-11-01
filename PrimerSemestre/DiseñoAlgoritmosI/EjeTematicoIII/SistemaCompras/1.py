def sistema_de_pagos():
    articulos = []
    total_articulos = 0
    total_precio = 0

    while True:
        nombre = input("Ingrese el nombre del artículo (o 'exit' para finalizar): ")
        if nombre.lower() == 'exit':
            break

        try:
            precio = float(input(f"Ingrese el precio de '{nombre}': "))
            cantidad = int(input(f"Ingrese la cantidad de '{nombre}': "))
            articulos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
            total_articulos += cantidad
            total_precio += precio * cantidad
        except ValueError:
            print("Por favor, ingrese un valor válido para el precio y la cantidad.")

    # Aplicar descuento basado en la cantidad de artículos
    if total_articulos >= 5:
        descuento = 0.20
        print("Descuento del 20% aplicado.")
    elif 3 <= total_articulos <= 4:
        descuento = 0.10
        print("Descuento del 10% aplicado.")
    else:
        descuento = 0.0
        print("No tienes descuento.")

    total_con_descuento = total_precio * (1 - descuento)

    # Determinar método de pago
    if total_articulos >= 3:
        metodo_pago = "Tarjeta"
        total_con_descuento *= 1.02  # Agregar 2% si es con tarjeta
    else:
        metodo_pago = "Efectivo"

    # Mostrar resumen de la compra
    print("\nResumen de la compra:")
    for articulo in articulos:
        print(f"{articulo['nombre']} - Precio: {articulo['precio']} - Cantidad: {articulo['cantidad']}")
    print(f"\nTotal de artículos: {total_articulos}")
    print(f"Total antes de descuento: {total_precio:.2f}")
    print(f"Total después de descuento: {total_con_descuento:.2f}")
    print(f"Método de pago: {metodo_pago}")
    print(f"Total final: {total_con_descuento:.2f}")
    

sistema_de_pagos()
