intereses = 0.04
dineroEnLaCuenta = float(input("Introduce la cantidad de dinero depositada en lacuenta de ahorros: "))
primerAno = dineroEnLaCuenta * (1 + intereses)
print("Ahorros el primer año: " + str(round(primerAno, 2)))
segundoAno = primerAno * (1 + intereses)
print("Ahorros el segundo año: " + str(round(segundoAno, 2)))
tercerAno = segundoAno * (1 + intereses)
print("Ahorros el tercer año: " + str(round(tercerAno, 2)))