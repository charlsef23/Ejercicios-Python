def rolpagos():
    acu = 0
    while True:
        try:
            n = int(input("INGRESE UNA CANTIDAD DE ROL DE PAGO: "))
            break
        except ValueError:
            print("ERROR: Ingrese un número válido.")

    for _ in range(n):
        nom = input("NOMBRE: ")
        while True:
            try:
                ht = int(input("HORAS TRABAJADAS: "))
                break
            except ValueError:
                print("::ERROR::")
        while True:
            try:
                vh = int(input("VALOR POR HORA: "))
                break
            except ValueError:
                print("ERROR")

        suel = ht * vh
        des = suel * 0.05 if suel < 300 else suel * 0.08
        net = suel - des
        acu += net
        print(f"NETO A RECIBIR ({nom}): {net:.2f}")
    print(f"TOTAL DE NETOS ACUMULADOS: {acu:.2f}")


def notas():
    c1 = c2 = 0
    while True:
        try:
            n = int(input("INGRESE NÚMERO DE ALUMNOS: "))
            break
        except ValueError:
            print("ERROR: Ingrese un número válido.")

    for _ in range(n):
        nom = input("NOMBRE: ")
        ac1 = 0
        for _ in range(2):
            while True:
                try:
                    nota = int(input("NOTA: "))
                    if 1 <= nota <= 10:
                        break
                    else:
                        print("NOTA NO VÁLIDA. Debe estar entre 1 y 10.")
                except ValueError:
                    print("ERROR: Ingrese un número válido.")
            ac1 += nota

        pro = ac1 / 2
        print(f"PROMEDIO DE {nom}: {pro:.2f}")
        if pro < 7:
            c1 += 1
            print("REPROBADO")
        else:
            c2 += 1
            print("APROBADO")

    print(f"CANTIDAD DE ALUMNOS APROBADOS: {c2}")
    print(f"CANTIDAD DE ALUMNOS REPROBADOS: {c1}")


def factura():
    mayor = menor = None
    prod_menor = prod_mayor = ""

    while True:
        try:
            n = int(input("INGRESE NÚMERO DE FACTURAS A REALIZAR: "))
            break
        except ValueError:
            print("ERROR: Ingrese un número válido.")

    for _ in range(n):
        prod = input("INGRESE PRODUCTO: ")
        while True:
            try:
                cant = int(input("INGRESE CANTIDAD: "))
                break
            except ValueError:
                print("ERROR")
        while True:
            try:
                pu = float(input("PRECIO UNITARIO: "))
                break
            except ValueError:
                print("ERROR")

        subtotal = cant * pu
        iva = subtotal * 0.12
        total = subtotal + iva
        print(f"TOTAL ({prod}): {total:.2f}")

        if menor is None or total < menor:
            menor = total
            prod_menor = prod
        if mayor is None or total > mayor:
            mayor = total
            prod_mayor = prod

    print(f"PRODUCTO CON MENOR COSTO: {prod_menor} (${menor:.2f})")
    print(f"PRODUCTO CON MAYOR COSTO: {prod_mayor} (${mayor:.2f})")


def menu_principal():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1) ROL DE PAGO")
        print("2) NOTAS")
        print("3) FACTURA")
        print("4) SALIR")
        try:
            opc = int(input("ESCOJA UNA OPCIÓN: "))
            if opc == 1:
                rolpagos()
            elif opc == 2:
                notas()
            elif opc == 3:
                factura()
            elif opc == 4:
                print("¡ADIOS!")
                break
            else:
                print("OPCIÓN NO VÁLIDA.")
        except ValueError:
            print("ERROR: Ingrese un número válido.")

menu_principal()