tarifas={
    "usa":900,
    "canada":800,
    "Europa":950,
    "Resto del mundo":1250,
}

destino=input("destino llamada: ")
duracion=int(input("duracion llamada: "))


total = tarifas[destino] * duracion

if duracion > 15:
    total = total - (total * 0.2)
    
    

print(total)
