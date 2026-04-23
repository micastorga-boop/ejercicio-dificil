#ejercicio dificil
total1 = 0

print("=== Cliente 1 ===")

pregunta = input("¿Quiere comida (si,no)?\n>").strip().lower()
if pregunta == "si": 
    tamanio = input("¿Que tamaño desea? (chico-$1500, mediano-$2500, grande-$3500)?\n>").strip().lower() 
    if tamanio == "chico":
        total1 += 1500
    elif tamanio == "mediano":
        total1 += 2500
    elif tamanio == "grande":
        total1 += 3500
    else:
        total1 += 2500
        print("Tamaño no reconocido, se cobrara el precio estandar, $2500.")

pregunta = input("¿Quiere bebida (si,no)?\n>").strip().lower()
if pregunta == "si":
    temperatura = input("¿Que tipo de bebida desea? (fria-$800, caliente-$1000)?\n>").strip().lower()
    if temperatura == "fria":
        total1 += 800
    elif temperatura == "caliente":
        total1 += 1000
    else:
        total1 += 800
        print("Tipo de bebida no reconocido, se cobrara el precio estandar, $800.")

    print("subtotal cliente 1:",total1)

    total2 = 0
    print("=== Cliente 2 ===")

pregunta = input("¿Quiere comida (si,no)?\n>").strip().lower()
if pregunta == "si": 
    tamanio = input("¿Que tamaño desea? (chico-$1500, mediano-$2500, grande-$3500)?\n>").strip().lower() 
    if tamanio == "chico":
        total2 += 1500
    elif tamanio == "mediano":
        total2 += 2500
    elif tamanio == "grande":
        total2   += 3500
    else:
        total2 += 2500
        print("Tamaño no reconocido, se cobrara el precio estandar, $2500.")

pregunta = input("¿Quiere bebida (si,no)?\n>").strip().lower()
if pregunta == "si":
    temperatura = input("¿Que tipo de bebida desea? (fria-$800, caliente-$1000)?\n>").strip().lower()
    if temperatura == "fria":
        total2 += 800
    elif temperatura == "caliente":
        total2 += 1000
    else:
        total2 += 800
        print("Tipo de bebida no reconocido, se cobrara el precio estandar, $800.")

    print("subtotal cliente 2:",total2)
total = total1 + total2
print("=== Total del turno ===")

print("Total del turno:", total)
if total > 8000:
    print("¡Turno de alto consumo! Total supera los $8000")
    