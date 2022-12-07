primitiva = []
for i in range(6):
    primitiva.append(int(input("Introduce un número ganador: ")))
primitiva.sort()
print("Los números ganadores son " + str(primitiva))