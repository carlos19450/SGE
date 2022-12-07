asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
suspendido = []
for asignatura in asignaturas:
    nota = float(input("¿Qué nota has sacado en " + asignatura + "?: "))
    if nota < 5:
        suspendido.append(asignatura)
for asignaturas in suspendido:
    print("Asignaturas a repetir: " + str(asignaturas))